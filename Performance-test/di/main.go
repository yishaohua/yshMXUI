package main

import (
	"time"
	"log"
	"os"
	"fmt"
	".."
	"github.com/pinterest/bender"
	bthrift "github.com/pinterest/bender/thrift"
	"git.apache.org/thrift.git/lib/go/thrift"
	"github.com/pinterest/bender/hist"
	"bufio"
	"strconv"
	"strings"
	"io"
)


func SyntheticRequests() chan interface{}{
        var num = 5000000
        c := make(chan interface{}, num)
        f, err := os.Open("/home/ec2-user/qa-test/pressure/mx-di/pressure/data/request.log")
        if err != nil {
                fmt.Print(err)
        }

        buf := bufio.NewReader(f)
        for ; len(c)<num-1; {
                line, error := buf.ReadString('\n')
                line = strings.TrimSpace(line)
                if error != nil || io.EOF == error {
                        break
                }
                idStart := strings.Index(line, "ids:[")
                idEnd := strings.Index(line, "], type")
                ids := line[idStart+5:idEnd]
                idArray := strings.Split(ids, ", ")

                typeStart := strings.Index(line, "type:")
                typeEnd := strings.Index(line, ", languageId")
                t := line[typeStart+5:typeEnd]

                var idwt di.IdsWithType
                idwt.Type = t
                idwt.Ids = idArray

                var req di.DIRequest
                req.IdsWithTypes = append(req.IdsWithTypes, &idwt)
                req.ServiceName = "test_client"

                c <- &req
        }

        close(c)
        return c
}
//重要:需要跟服务端所用协议一致
func ASExecutor(request interface{}, transport thrift.TTransport) (interface{}, error) {
	pFac := thrift.NewTCompactProtocolFactory()

	client := di.NewDIServiceClientFactory(transport, pFac)
	return client.GetDetail(nil, request.(*di.DIRequest))
}

// 主要是用bender的接口，完成压测
func main() {
	//intervals := bender.ExponentialIntervalGenerator(300)
        qpsTarget , err := strconv.ParseFloat(os.Args[1], 64)
        fmt.Println(err)
        intervals := bender.ExponentialIntervalGenerator(qpsTarget) // qps
	requests := SyntheticRequests()          // 总请求数

	//host := "di.dev.mxplay.com:8082"
        //host := "di.dev.mxplay.com:8082" //press机器
       // host := "ec2-13-232-94-32.ap-south-1.compute.amazonaws.com:19959" //press机器
        host :="ec2-13-126-169-27.ap-south-1.compute.amazonaws.com:29999"
	//host := "ec2-52-66-188-192.ap-south-1.compute.amazonaws.com:19959" //press机器
	//buffer字节数, clientExec, 超时时间, hosts--写server所在的ip和端口,如非同一机器,保证端口可访问
	//exec := bthrift.NewThriftRequestExec(thrift.NewTBufferedTransportFactory(125), ASExecutor, 10 * time.Second, host)
	//exec := bthrift.NewThriftRequestExec(thrift.NewTCompactProtocolFactory(), ASExecutor, 10 * time.Second, host)
	exec := bthrift.NewThriftRequestExec(thrift.NewTFramedTransportFactory(thrift.NewTTransportFactory()), ASExecutor, 10 * time.Second, host)
	recorder := make(chan interface{}, 128)
	bender.LoadTestThroughput(intervals, requests, exec, recorder)
	l := log.New(os.Stdout, "", log.LstdFlags)
	h := hist.NewHistogram(60000, 1000000)
	bender.Record(recorder, bender.NewLoggingRecorder(l), bender.NewHistogramRecorder(h))
	fmt.Println(h)
}
