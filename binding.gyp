{
  "targets": [
    {
      "target_name": "<(module_name)",
      "cflags_cc": [ "-std=c++17" ],
      "cflags!": [ "-fno-exceptions", "-fno-rtti" ],
      "cflags_cc!": [ "-fno-exceptions", "-fno-rtti" ],
      "link_settings": {
          "libraries": [
              "-ljpeg",
              "-lpng",
              "../rust_native_storage_library/target/debug/librust_native_storage_library.a",
              "/usr/local/lib/libtensorflow.so",
              "/usr/local/lib/libtensorflow_framework.so",
              "/usr/lib/llvm-10/lib/libLLVM.so",
              "/usr/lib/llvm-10/lib/liblldELF.a",
              "/usr/lib/llvm-10/lib/liblldCommon.a",
              "/usr/lib/llvm-10/lib/liblldCore.a",
              "/usr/lib/llvm-10/lib/liblldDriver.a",
              "/usr/lib/llvm-10/lib/liblldReaderWriter.a",
              "/usr/lib/llvm-10/lib/liblldYAML.a",
          ],
      },
      "sources": [
        "ssvmaddon.cc",
        "ssvm-napi/addon.cc",
        "ssvm-napi/bytecode.cc",
        "ssvm-napi/options.cc",
        "ssvm-napi/utils.cc",
        "ssvm-napi/ssvm-core/lib/aot/compiler.cpp",
        "ssvm-napi/ssvm-core/lib/ast/description.cpp",
        "ssvm-napi/ssvm-core/lib/ast/expression.cpp",
        "ssvm-napi/ssvm-core/lib/ast/instruction.cpp",
        "ssvm-napi/ssvm-core/lib/ast/module.cpp",
        "ssvm-napi/ssvm-core/lib/ast/section.cpp",
        "ssvm-napi/ssvm-core/lib/ast/segment.cpp",
        "ssvm-napi/ssvm-core/lib/ast/type.cpp",
        "ssvm-napi/ssvm-core/lib/common/hexstr.cpp",
        "ssvm-napi/ssvm-core/lib/common/log.cpp",
        "ssvm-napi/ssvm-core/lib/host/ssvm_process/processfunc.cpp",
        "ssvm-napi/ssvm-core/lib/host/ssvm_process/processmodule.cpp",
        "ssvm-napi/ssvm-core/lib/host/wasi/wasienv.cpp",
        "ssvm-napi/ssvm-core/lib/host/wasi/wasifunc.cpp",
        "ssvm-napi/ssvm-core/lib/host/wasi/wasimodule.cpp",
        "ssvm-napi/ssvm-core/lib/interpreter/engine/control.cpp",
        "ssvm-napi/ssvm-core/lib/interpreter/engine/engine.cpp",
        "ssvm-napi/ssvm-core/lib/interpreter/engine/memory.cpp",
        "ssvm-napi/ssvm-core/lib/interpreter/engine/table.cpp",
        "ssvm-napi/ssvm-core/lib/interpreter/engine/variable.cpp",
        "ssvm-napi/ssvm-core/lib/interpreter/instantiate/data.cpp",
        "ssvm-napi/ssvm-core/lib/interpreter/instantiate/elem.cpp",
        "ssvm-napi/ssvm-core/lib/interpreter/instantiate/export.cpp",
        "ssvm-napi/ssvm-core/lib/interpreter/instantiate/function.cpp",
        "ssvm-napi/ssvm-core/lib/interpreter/instantiate/global.cpp",
        "ssvm-napi/ssvm-core/lib/interpreter/instantiate/import.cpp",
        "ssvm-napi/ssvm-core/lib/interpreter/instantiate/memory.cpp",
        "ssvm-napi/ssvm-core/lib/interpreter/instantiate/module.cpp",
        "ssvm-napi/ssvm-core/lib/interpreter/instantiate/table.cpp",
        "ssvm-napi/ssvm-core/lib/interpreter/interpreter.cpp",
        "ssvm-napi/ssvm-core/lib/loader/filemgr.cpp",
        "ssvm-napi/ssvm-core/lib/loader/ldmgr.cpp",
        "ssvm-napi/ssvm-core/lib/loader/loader.cpp",
        "ssvm-napi/ssvm-core/lib/validator/formchecker.cpp",
        "ssvm-napi/ssvm-core/lib/validator/validator.cpp",
        "ssvm-napi/ssvm-core/lib/vm/vm.cpp",
        "ssvm-napi/ssvm-core/thirdparty/easyloggingpp/easylogging++.cc",
        "ssvm-storage/lib/storage_func.cpp",
        "ssvm-storage/lib/storage_module.cpp",
        "ssvm-tensorflow/lib/tensorflow_func.cpp",
        "ssvm-tensorflow/lib/tensorflow_module.cpp",
      ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")",
        "ssvm-napi",
        "ssvm-napi/ssvm-core/include",
        "ssvm-napi/ssvm-core/thirdparty",
        "ssvm-napi/ssvm-core/thirdparty/googletest/include",
        "ssvm-storage/include",
        "ssvm-tensorflow/include",
        "rust_native_storage_library/src",
        "/usr/lib/llvm-10/include",
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
