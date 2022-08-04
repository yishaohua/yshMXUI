
VERSION_CODE_CHECK_BLACK_LIST = ['com.mxtech.videoplayer.share', 'com.young.simple.player', 'com.mxtech.live']
TEXTREL_CHECK_BLACK_LIST = ['com.mxtech.videoplayer.share', 'com.next.innovation.takatak', 'com.mxtech.videoplayer.online', 'com.young.simple.player']

VERSION_CODE_PREFIX = {
    'com.mxtech.videoplayer.ad': {
        'neon': {
            'armeabi-v7a': '131',
            'arm64-v8a': '133'
        },
        'x86': {
            'x86': '137',
            'x86_64': '138'
        }
    },
    'com.mxtech.videoplayer.pro': {
        'neon': {
            'armeabi-v7a': '131',
            'arm64-v8a': '133'
        },
        'x86': {
            'x86': '13700',
            'x86_64': '13800'
        }
    },
    'com.mxtech.videoplayer.beta': {
        'neon': {
            'armeabi-v7a': '117',
            'arm64-v8a': '135'
        }

    },
    'com.next.innovation.takatak':{
        'neon': {
            'armeabi-v7a': '100',
            'arm64-v8a': '200'
        }
    },
    'com.next.innovation.takatak.debug': {
        'neon': {
            'armeabi-v7a': '100',
            'arm64-v8a': '200'
        }
    },
    'com.mxtech.videoplayer.online': {
        'neon': {
            'armeabi-v7a': '131',
            'arm64-v8a': '133'
        }
    }
}

PERMISSIONS = {
    'com.mxtech.videoplayer.ad': [
        'android.permission.ACCESS_NETWORK_STATE',
        'android.permission.ACCESS_WIFI_STATE',
        'android.permission.INTERNET',
        'android.permission.WRITE_EXTERNAL_STORAGE',
        'android.permission.SYSTEM_ALERT_WINDOW',
        'android.permission.KILL_BACKGROUND_PROCESSES',
        'android.permission.WAKE_LOCK',
        'android.permission.BLUETOOTH',
        'android.permission.VIBRATE',
        'android.permission.DISABLE_KEYGUARD',
        'com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE',
        'android.permission.READ_EXTERNAL_STORAGE',
        'com.google.android.c2dm.permission.RECEIVE',
        'com.mxtech.videoplayer.ad.permission.C2D_MESSAGE',
        'android.permission.FOREGROUND_SERVICE',
        'android.permission.CHANGE_NETWORK_STATE',
        'android.permission.CHANGE_WIFI_STATE',
        'android.permission.ACCESS_COARSE_LOCATION',
        'android.permission.ACCESS_FINE_LOCATION',
        'android.permission.WRITE_SETTINGS',
        'android.permission.CAMERA',
        'android.permission.FLASHLIGHT',
        'android.permission.BLUETOOTH_ADMIN',
        'android.permission.RECEIVE_USER_PRESENT',
        'android.permission.REQUEST_INSTALL_PACKAGES',
        'android.permission.MANAGE_EXTERNAL_STORAGE',
        'com.huawei.appmarket.service.commondata.permission.GET_COMMON_DATA',
        'android.permission.READ_PHONE_NUMBERS',
        'android.permission.RECORD_AUDIO',
        'android.permission.INSTALL_SHORTCUT'
    ],
    'com.mxtech.videoplayer.pro': [
        'android.permission.ACCESS_NETWORK_STATE',
        'android.permission.ACCESS_WIFI_STATE',
        'android.permission.INTERNET',
        'android.permission.WRITE_EXTERNAL_STORAGE',
        'android.permission.SYSTEM_ALERT_WINDOW',
        'android.permission.KILL_BACKGROUND_PROCESSES',
        'android.permission.WAKE_LOCK',
        'android.permission.BLUETOOTH',
        'android.permission.VIBRATE',
        'android.permission.DISABLE_KEYGUARD',
        'com.android.vending.CHECK_LICENSE',
        'android.permission.READ_EXTERNAL_STORAGE',
        'com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE',
        'com.google.android.c2dm.permission.RECEIVE',
        'com.mxtech.videoplayer.pro.permission.C2D_MESSAGE',
        'android.permission.FOREGROUND_SERVICE',
        'android.permission.GET_ACCOUNTS',
        'android.permission.CHANGE_NETWORK_STATE',
        'android.permission.CHANGE_WIFI_STATE',
        'android.permission.ACCESS_COARSE_LOCATION',
        'android.permission.ACCESS_FINE_LOCATION',
        'android.permission.WRITE_SETTINGS',
        'android.permission.CAMERA',
        'android.permission.FLASHLIGHT',
        'android.permission.BLUETOOTH_ADMIN',
        'android.permission.RECEIVE_USER_PRESENT',
        'android.permission.REQUEST_INSTALL_PACKAGES',
        'android.permission.MANAGE_EXTERNAL_STORAGE'
    ],
    'com.mxtech.videoplayer.beta': [
        'android.permission.ACCESS_NETWORK_STATE',
        'android.permission.ACCESS_WIFI_STATE',
        'android.permission.INTERNET',
        'android.permission.WRITE_EXTERNAL_STORAGE',
        'android.permission.SYSTEM_ALERT_WINDOW',
        'android.permission.KILL_BACKGROUND_PROCESSES',
        'android.permission.WAKE_LOCK',
        'android.permission.BLUETOOTH',
        'android.permission.VIBRATE',
        'android.permission.DISABLE_KEYGUARD',
        'com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE',
        'android.permission.READ_EXTERNAL_STORAGE',
        'com.google.android.c2dm.permission.RECEIVE',
        'com.mxtech.videoplayer.beta.permission.C2D_MESSAGE',
        'android.permission.FOREGROUND_SERVICE',
        'android.permission.CHANGE_NETWORK_STATE',
        'android.permission.CHANGE_WIFI_STATE',
        'android.permission.ACCESS_COARSE_LOCATION',
        'android.permission.ACCESS_FINE_LOCATION',
        'android.permission.WRITE_SETTINGS',
        'android.permission.CAMERA',
        'android.permission.FLASHLIGHT',
        'android.permission.BLUETOOTH_ADMIN',
        'android.permission.RECEIVE_USER_PRESENT',
        'android.permission.REQUEST_INSTALL_PACKAGES',
        'android.permission.MANAGE_EXTERNAL_STORAGE'
    ],
    'com.mxtech.videoplayer.television': [
        'android.permission.ACCESS_NETWORK_STATE',
        'android.permission.ACCESS_WIFI_STATE',
        'android.permission.INTERNET',
        'android.permission.WRITE_EXTERNAL_STORAGE',
        'android.permission.WAKE_LOCK',
        'com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE',
        'com.google.android.c2dm.permission.RECEIVE',
        'com.amazon.device.permission.COMRADE_CAPABILITIES'
    ],
    'com.next.innovation.takatak': [
        'android.permission.ACCESS_NETWORK_STATE',
        'android.permission.INTERNET',
        'android.permission.WRITE_EXTERNAL_STORAGE',
        'android.permission.READ_EXTERNAL_STORAGE',
        'android.permission.WAKE_LOCK',
        'android.permission.ACCESS_FINE_LOCATION',
        'android.permission.ACCESS_WIFI_STATE',
        'android.permission.READ_PHONE_STATE',
        'android.permission.CALL_PHONE',
        'android.permission.RECORD_AUDIO',
        'android.permission.CAMERA',
        'android.permission.READ_CONTACTS',
        'android.permission.ACCESS_COARSE_LOCATION',
        'android.permission.CHANGE_NETWORK_STATE',
        'android.permission.GET_TASKS',
        'android.permission.MODIFY_AUDIO_SETTINGS',
        'android.permission.RECEIVE_BOOT_COMPLETED',
        'android.permission.VIBRATE',
        'android.permission.SYSTEM_ALERT_WINDOW',
        'android.permission.GET_ACCOUNTS',
        'android.permission.USE_CREDENTIALS',
        'android.permission.MANAGE_ACCOUNTS',
        'android.permission.BLUETOOTH',
        'android.permission.READ_LOGS',
        'com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE',
        'com.google.android.c2dm.permission.RECEIVE',
        'com.next.innovation.takatak.permission.C2D_MESSAGE',
        'android.permission.FOREGROUND_SERVICE',
        'com.next.innovation.takatak.permission.MIPUSH_RECEIVE',
        'android.permission.REQUEST_INSTALL_PACKAGES',
        'android.permission.BLUETOOTH_CONNECT',
        'android.permission.READ_PHONE_NUMBERS'
    ],
    'com.next.innovation.takatak.debug': [
        'android.permission.ACCESS_NETWORK_STATE',
        'android.permission.INTERNET',
        'android.permission.WRITE_EXTERNAL_STORAGE',
        'android.permission.READ_EXTERNAL_STORAGE',
        'android.permission.WAKE_LOCK',
        'android.permission.ACCESS_FINE_LOCATION',
        'android.permission.ACCESS_WIFI_STATE',
        'android.permission.READ_PHONE_STATE',
        'android.permission.CALL_PHONE',
        'android.permission.RECORD_AUDIO',
        'android.permission.CAMERA',
        'android.permission.READ_CONTACTS',
        'android.permission.ACCESS_COARSE_LOCATION',
        'android.permission.CHANGE_NETWORK_STATE',
        'android.permission.GET_TASKS',
        'android.permission.MODIFY_AUDIO_SETTINGS',
        'android.permission.RECEIVE_BOOT_COMPLETED',
        'android.permission.VIBRATE',
        'android.permission.SYSTEM_ALERT_WINDOW',
        'android.permission.GET_ACCOUNTS',
        'android.permission.USE_CREDENTIALS',
        'android.permission.MANAGE_ACCOUNTS',
        'android.permission.BLUETOOTH',
        'android.permission.READ_LOGS',
        'com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE',
        'com.google.android.c2dm.permission.RECEIVE',
        'com.next.innovation.takatak.permission.C2D_MESSAGE',
        'android.permission.FOREGROUND_SERVICE',
        'com.next.innovation.takatak.permission.MIPUSH_RECEIVE',
        'android.permission.REQUEST_INSTALL_PACKAGES',
        'android.permission.READ_PHONE_NUMBERS'
    ],
    'com.mxtech.videoplayer.share': [
        'android.permission.ACCESS_NETWORK_STATE',
        'android.permission.CHANGE_NETWORK_STATE',
        'android.permission.ACCESS_WIFI_STATE',
        'android.permission.CHANGE_WIFI_STATE',
        'android.permission.ACCESS_COARSE_LOCATION',
        'android.permission.ACCESS_FINE_LOCATION',
        'android.permission.WRITE_SETTINGS',
        'android.permission.WRITE_EXTERNAL_STORAGE',
        'android.permission.CAMERA',
        'android.permission.INTERNET',
        'android.permission.VIBRATE',
        'android.permission.FLASHLIGHT',
        'android.permission.BLUETOOTH',
        'android.permission.BLUETOOTH_ADMIN',
        'android.permission.WAKE_LOCK',
        'android.permission.REQUEST_INSTALL_PACKAGES',
        'com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE',
        'com.google.android.c2dm.permission.RECEIVE',
        'android.permission.READ_EXTERNAL_STORAGE',
        'android.permission.FOREGROUND_SERVICE',
        'android.permission.MANAGE_EXTERNAL_STORAGE'
        ],
    'com.mxtech.videoplayer.online': [
        'android.permission.FOREGROUND_SERVICE',
        'android.permission.ACCESS_NETWORK_STATE',
        'android.permission.ACCESS_WIFI_STATE',
        'android.permission.INTERNET',
        'android.permission.WRITE_EXTERNAL_STORAGE',
        'android.permission.SYSTEM_ALERT_WINDOW',
        'android.permission.KILL_BACKGROUND_PROCESSES',
        'android.permission.WAKE_LOCK',
        'android.permission.BLUETOOTH',
        'android.permission.VIBRATE',
        'android.permission.DISABLE_KEYGUARD',
        'com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE',
        'android.permission.CHANGE_NETWORK_STATE',
        'android.permission.CHANGE_WIFI_STATE',
        'android.permission.ACCESS_COARSE_LOCATION',
        'android.permission.ACCESS_FINE_LOCATION',
        'android.permission.WRITE_SETTINGS',
        'android.permission.CAMERA',
        'android.permission.FLASHLIGHT',
        'android.permission.BLUETOOTH_ADMIN',
        'android.permission.REQUEST_INSTALL_PACKAGES',
        'android.permission.RECEIVE_USER_PRESENT',
        'com.google.android.c2dm.permission.RECEIVE',
        'android.permission.READ_EXTERNAL_STORAGE'
    ],
    'com.mxtech.live': [
        'android.permission.ACCESS_NETWORK_STATE',
        'android.permission.INTERNET',
        'android.permission.WRITE_EXTERNAL_STORAGE',
        'android.permission.READ_EXTERNAL_STORAGE',
        'android.permission.WAKE_LOCK',
        'android.permission.CAMERA',
        'android.permission.ACCESS_WIFI_STATE',
        'android.permission.RECORD_AUDIO',
        'android.permission.MODIFY_AUDIO_SETTINGS',
        'android.permission.BLUETOOTH',
        'android.permission.READ_PHONE_STATE',
        'android.permission.VIBRATE',
        'android.permission.RECEIVE_BOOT_COMPLETED',
        'android.permission.READ_PHONE_NUMBERS',
        'com.google.android.c2dm.permission.RECEIVE',
        'android.permission.FOREGROUND_SERVICE',
        'com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE',
        'android.permission.BLUETOOTH_CONNECT',
        'android.permission.SYSTEM_ALERT_WINDOW'
    ],
    'com.young.simple.player': [
        'android.permission.ACCESS_NETWORK_STATE',
        'android.permission.FOREGROUND_SERVICE',
        'android.permission.ACCESS_NETWORK_STATE',
        'android.permission.ACCESS_WIFI_STATE',
        'android.permission.INTERNET',
        'android.permission.READ_EXTERNAL_STORAGE',
        'android.permission.WRITE_EXTERNAL_STORAGE',
        'android.permission.WAKE_LOCK',
        'android.permission.DISABLE_KEYGUARD',
        'com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE'
    ]
}

LAUNCH_MODE_CHECK_BLACK_LIST = ['com.google.android.play.core.missingsplits.PlayCoreMissingSplitsActivity']
