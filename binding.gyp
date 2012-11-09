{
   "targets": [
      {
         "target_name": "couchbase_impl",
         "sources": [
            "src/args.c",
            "src/couchbase_impl.c",
            "src/namemap.c",
            "src/notify.c",
            "src/operations.c",
            "src/cas.c",
            "io/common.cc",
            "io/socket.cc",
            "io/read.cc",
            "io/write.cc",
            "io/timer.cc",
            "io/plugin-libuv.cc",
            "io/util/lcb_luv_yolog.cc",
            "io/util/hexdump.cc"
         ],
         'cflags': [ '-I..' ],
         'cflags!': [
            '-fno-exceptions'
         ],
         'cflags_cc!': [ '-fno-exceptions' ],
         'conditions': [
           ['OS=="mac"', {
             'xcode_settings': {
               'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
               'OTHER_CFLAGS': [ '-I..' ]
             }
           }]
         ],
         'link_settings': {
           'ldflags': [
             '-lcouchbase'
           ],
           'libraries': [
             '-lcouchbase'
           ]
         }
      }
   ]
}
