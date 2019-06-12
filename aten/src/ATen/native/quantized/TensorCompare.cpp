#include <ATen/ATen.h>
#include <ATen/CPUApplyUtils.h>
#include <ATen/Dispatch.h>
#include <ATen/ExpandUtils.h>
#include <ATen/NativeFunctions.h>
#include <ATen/native/ReduceOpsUtils.h>
#include <c10/util/Exception.h>
#include <ATen/native/cpu/TensorCompareKernel.h>

namespace at { namespace native {

Tensor max_quant(const Tensor& self) {
  return std::get<0>(self.reshape({-1}).max(/*dim=*/0));
}

Tensor min_quant(const Tensor& self) {
  return std::get<0>(self.reshape({-1}).min(/*dim=*/0));
}

// TODO: move to TensorMath.cpp

std::tuple<Tensor, Tensor> sort(const Tensor& self, int64_t dim, bool descending) {
  if (self.is_quantized()) {
    Tensor sort_int;
    Tensor sort_indicies;
    std::tie(sort_int, sort_indicies) = at::sort(self.int_repr(), dim, descending);
    return std::forward_as_tuple(
      at::_per_tensor_affine_qtensor(
        sort_int,
        self.q_scale(),
        self.q_zero_point()),
        sort_indicies);
  } else {
    return at::sort(self, dim, descending);
  }
}

}} // namespace at::native
