#include <ATen/native/mkldnn/MKLDNNCommon.h>

namespace at { namespace native {

#if AT_MKLDNN_ENABLED()

Tensor empty_mkldnn(IntArrayRef sizes, const TensorOptions& options) {
  // NOTE: int32_t dims from ideep::tensor but sizes needs int64_t
  // TODO: support int64_t dims in ideep::tensor to avoid extra conversion
  ideep::tensor::dims dst_dims (sizes.begin(), sizes.end());
  ideep::tensor it;
  it.resize<AllocForMKLDNN>(dst_dims, ideep::tensor::data_type::f32);
  return new_with_itensor_mkldnn(std::move(it), options);
}

#else

Tensor empty_mkldnn(IntArrayRef sizes, const TensorOptions& options) {
  AT_ERROR("empty_mkldnn: MKL-DNN build is disabled");
}

#endif // AT_MKLDNN_ENABLED()

}}
