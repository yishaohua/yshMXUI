# !/bin/bash
# -*- coding: utf-8 -*-
# 这个脚本会自动测试 apk 启动时间，共执行 10 次。提供首次安装启动、冷启动、热启动可供选择。


firstLaunch(){


    echo "start first launch 10 times"
    for i in {1..10}
    do
        echo "-----第 $i 次首次启动测试-----"
        uninstallApp
        installApp
        TotalTime[i]=`adb shell am start -W $PackageName/$ActivityName |grep TotalTime|awk -F ' ' '{print $2}'|tr -d "\r"`
        sleep 3s
        echo ${TotalTime[i]}
    done
    max=0
    for n in "${TotalTime[@]}"
    do
        ((n>max)) && max=$n
    done
    echo "首次启动峰值:$max ms"

    avg=0
    sum=$((${TotalTime[1]} + ${TotalTime[2]} + ${TotalTime[3]} + ${TotalTime[4]} + ${TotalTime[5]} + ${TotalTime[6]} + ${TotalTime[7]} + ${TotalTime[8]} + ${TotalTime[9]} + ${TotalTime[10]}))
    avg=$[$sum/10]
    echo "首次启动均值:$avg ms"
}


installApp(){

    echo "----重新安装被测APP $PackageName ----"
    apps_dir=$(pwd)
    echo $apps_dir
    adb install $apps_dir/appStartTest/$PackageName.apk

}

uninstallApp(){
    echo "-----开始卸载被测App $PackageName-----"
    adb uninstall $PackageName
}



echo "请输入被测包名："
read PackageName
echo "请输入启动Activity："
read ActivityName

firstLaunch


echo "----测试结束----"