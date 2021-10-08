{
  "targets": [
    {
      "target_name": "<(module_name)",
      "cflags_cc": [ "-std=c++17" ],
      "cflags!": [ "-fno-exceptions", "-fno-rtti" ],
      "cflags_cc!": [ "-fno-exceptions", "-fno-rtti" ],
      "link_settings": {
          "libraries": [
              "$(HOME)/.wasmedge/lib/libwasmedge-tensorflow_c.so",
              "$(HOME)/.wasmedge/lib/libwasmedge-tensorflowlite_c.so",
              "$(HOME)/.wasmedge/lib/libwasmedge-image_c.so",
              "$(HOME)/.wasmedge/lib/libwasmedge_c.so",
              "$(HOME)/.wasmedge/lib/libtensorflow.so",
              "$(HOME)/.wasmedge/lib/libtensorflow_framework.so",
              "$(HOME)/.wasmedge/lib/libtensorflowlite_c.so",
              "$(HOME)/.wasmedge/lib/libjpeg.so",
              "$(HOME)/.wasmedge/lib/libpng.so",
          ]
      },
      "sources": [
        "wasmedgeaddon.cc",
        "wasmedge-core/src/addon.cc",
        "wasmedge-core/src/bytecode.cc",
        "wasmedge-core/src/options.cc",
        "wasmedge-core/src/utils.cc",
      ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")",
        "wasmedge-core/src",
        "$(HOME)/.wasmedge/include",
      ],
      'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
    },
    {
      "target_name": "action_after_build",
      "type": "none",
      "dependencies": [ "<(module_name)" ],
      "copies": [
        {
          "files": [ "<(PRODUCT_DIR)/<(module_name).node" ],
          "destination": "<(module_path)"
        }
      ]
    }
  ]
}
