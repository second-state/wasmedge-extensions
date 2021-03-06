#pragma once

#include <cstdint>
#include <string>
#include <vector>

namespace WASMEDGE {
namespace NAPI {

class Bytecode {
public:
  enum class InputMode {
    Invalid,
    FilePath,
    WasmBytecode,
    ELFBytecode,
    MachOBytecode
  };

private:
  std::vector<uint8_t> Data;
  std::string Path;
  InputMode Mode;

public:
  void setPath(const std::string &IPath) noexcept;
  const std::string &getPath() const noexcept { return Path; }
  void setData(const std::vector<uint8_t> &IData) noexcept;
  const std::vector<uint8_t> &getData() noexcept;
  void setFileMode() noexcept;
  bool isFile() const noexcept;
  bool isWasm() const noexcept;
  bool isELF() const noexcept;
  bool isMachO() const noexcept;
  bool isCompiled() const noexcept;
  bool isValidData() const noexcept;
};

} // namespace NAPI
} // namespace WASMEDGE
