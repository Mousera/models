# Copyright 2019 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Test utils for other test files."""

# import tensorflow as tf
#
# from vision.object.methods.cnn.models.slim.nets import mobilenet_v1
#
# slim = tf.contrib.slim
#
# # Layer names of Slim to map Keras layer names in MobilenetV1
# _MOBLIENET_V1_SLIM_ENDPOINTS = [
#     'Conv2d_0',
#     'Conv2d_1_depthwise', 'Conv2d_1_pointwise',
#     'Conv2d_2_depthwise', 'Conv2d_2_pointwise',
#     'Conv2d_3_depthwise', 'Conv2d_3_pointwise',
#     'Conv2d_4_depthwise', 'Conv2d_4_pointwise',
#     'Conv2d_5_depthwise', 'Conv2d_5_pointwise',
#     'Conv2d_6_depthwise', 'Conv2d_6_pointwise',
#     'Conv2d_7_depthwise', 'Conv2d_7_pointwise',
#     'Conv2d_8_depthwise', 'Conv2d_8_pointwise',
#     'Conv2d_9_depthwise', 'Conv2d_9_pointwise',
#     'Conv2d_10_depthwise', 'Conv2d_10_pointwise',
#     'Conv2d_11_depthwise', 'Conv2d_11_pointwise',
#     'Conv2d_12_depthwise', 'Conv2d_12_pointwise',
#     'Conv2d_13_depthwise', 'Conv2d_13_pointwise'
# ]
#
#
# # Function to get the output shape of each layer in Slim. It's used to
# # generate the following constant expected_feature_map_shape for MobilenetV1.
# # Similarly, this can also apply to MobilenetV2.
# def _get_slim_endpoint_shapes(inputs, depth_multiplier=1.0, min_depth=8,
#                               use_explicit_padding=False):
#   with slim.arg_scope([slim.conv2d, slim.separable_conv2d],
#                       normalizer_fn=slim.batch_norm):
#     _, end_points = mobilenet_v1.mobilenet_v1_base(
#         inputs, final_endpoint='Conv2d_13_pointwise',
#         depth_multiplier=depth_multiplier, min_depth=min_depth,
#         use_explicit_padding=use_explicit_padding)
#     return [end_points[endpoint_name].get_shape()
#             for endpoint_name in _MOBLIENET_V1_SLIM_ENDPOINTS]


# For Mobilenet V1
moblenet_v1_expected_feature_map_shape_128 = [
    (2, 64, 64, 32), (2, 64, 64, 32), (2, 64, 64, 64), (2, 32, 32, 64),
    (2, 32, 32, 128), (2, 32, 32, 128), (2, 32, 32, 128), (2, 16, 16, 128),
    (2, 16, 16, 256), (2, 16, 16, 256), (2, 16, 16, 256), (2, 8, 8, 256),
    (2, 8, 8, 512), (2, 8, 8, 512), (2, 8, 8, 512), (2, 8, 8, 512),
    (2, 8, 8, 512), (2, 8, 8, 512), (2, 8, 8, 512), (2, 8, 8, 512),
    (2, 8, 8, 512), (2, 8, 8, 512), (2, 8, 8, 512), (2, 4, 4, 512),
    (2, 4, 4, 1024), (2, 4, 4, 1024), (2, 4, 4, 1024),
]

moblenet_v1_expected_feature_map_shape_128_explicit_padding = [
    (2, 64, 64, 32), (2, 64, 64, 32), (2, 64, 64, 64), (2, 32, 32, 64),
    (2, 32, 32, 128), (2, 32, 32, 128), (2, 32, 32, 128), (2, 16, 16, 128),
    (2, 16, 16, 256), (2, 16, 16, 256), (2, 16, 16, 256), (2, 8, 8, 256),
    (2, 8, 8, 512), (2, 8, 8, 512), (2, 8, 8, 512), (2, 8, 8, 512),
    (2, 8, 8, 512), (2, 8, 8, 512), (2, 8, 8, 512), (2, 8, 8, 512),
    (2, 8, 8, 512), (2, 8, 8, 512), (2, 8, 8, 512), (2, 4, 4, 512),
    (2, 4, 4, 1024), (2, 4, 4, 1024), (2, 4, 4, 1024),
]

mobilenet_v1_expected_feature_map_shape_with_dynamic_inputs = [
    (2, 64, 64, 32), (2, 64, 64, 32), (2, 64, 64, 64), (2, 32, 32, 64),
    (2, 32, 32, 128), (2, 32, 32, 128), (2, 32, 32, 128), (2, 16, 16, 128),
    (2, 16, 16, 256), (2, 16, 16, 256), (2, 16, 16, 256), (2, 8, 8, 256),
    (2, 8, 8, 512), (2, 8, 8, 512), (2, 8, 8, 512), (2, 8, 8, 512),
    (2, 8, 8, 512), (2, 8, 8, 512), (2, 8, 8, 512), (2, 8, 8, 512),
    (2, 8, 8, 512), (2, 8, 8, 512), (2, 8, 8, 512), (2, 4, 4, 512),
    (2, 4, 4, 1024), (2, 4, 4, 1024), (2, 4, 4, 1024),
]

moblenet_v1_expected_feature_map_shape_299 = [
    (2, 150, 150, 32), (2, 150, 150, 32), (2, 150, 150, 64), (2, 75, 75, 64),
    (2, 75, 75, 128), (2, 75, 75, 128), (2, 75, 75, 128), (2, 38, 38, 128),
    (2, 38, 38, 256), (2, 38, 38, 256), (2, 38, 38, 256), (2, 19, 19, 256),
    (2, 19, 19, 512), (2, 19, 19, 512), (2, 19, 19, 512), (2, 19, 19, 512),
    (2, 19, 19, 512), (2, 19, 19, 512), (2, 19, 19, 512), (2, 19, 19, 512),
    (2, 19, 19, 512), (2, 19, 19, 512), (2, 19, 19, 512), (2, 10, 10, 512),
    (2, 10, 10, 1024), (2, 10, 10, 1024), (2, 10, 10, 1024),
]

moblenet_v1_expected_feature_map_shape_enforcing_min_depth = [
    (2, 150, 150, 8), (2, 150, 150, 8), (2, 150, 150, 8), (2, 75, 75, 8),
    (2, 75, 75, 8), (2, 75, 75, 8), (2, 75, 75, 8), (2, 38, 38, 8),
    (2, 38, 38, 8), (2, 38, 38, 8), (2, 38, 38, 8), (2, 19, 19, 8),
    (2, 19, 19, 8), (2, 19, 19, 8), (2, 19, 19, 8), (2, 19, 19, 8),
    (2, 19, 19, 8), (2, 19, 19, 8), (2, 19, 19, 8), (2, 19, 19, 8),
    (2, 19, 19, 8), (2, 19, 19, 8), (2, 19, 19, 8), (2, 10, 10, 8),
    (2, 10, 10, 8), (2, 10, 10, 8), (2, 10, 10, 8),
]

moblenet_v1_expected_feature_map_shape_with_conv_defs = [
    (2, 150, 150, 32), (2, 150, 150, 32), (2, 150, 150, 64), (2, 75, 75, 64),
    (2, 75, 75, 128), (2, 75, 75, 128), (2, 75, 75, 128), (2, 38, 38, 128),
    (2, 38, 38, 256), (2, 38, 38, 256), (2, 38, 38, 256), (2, 19, 19, 256),
    (2, 19, 19, 512), (2, 19, 19, 512), (2, 19, 19, 512), (2, 19, 19, 512),
    (2, 19, 19, 512), (2, 19, 19, 512), (2, 19, 19, 512), (2, 19, 19, 512),
    (2, 19, 19, 512), (2, 19, 19, 512), (2, 19, 19, 512), (2, 10, 10, 512),
    (2, 10, 10, 512), (2, 10, 10, 512), (2, 10, 10, 256),
]

# For Mobilenet V2
moblenet_v2_expected_feature_map_shape_128 = [
    (2, 64, 64, 32), (2, 64, 64, 96), (2, 32, 32, 96), (2, 32, 32, 24),
    (2, 32, 32, 144), (2, 32, 32, 144), (2, 32, 32, 24), (2, 32, 32, 144),
    (2, 16, 16, 144), (2, 16, 16, 32), (2, 16, 16, 192), (2, 16, 16, 192),
    (2, 16, 16, 32), (2, 16, 16, 192), (2, 16, 16, 192), (2, 16, 16, 32),
    (2, 16, 16, 192), (2, 8, 8, 192), (2, 8, 8, 64), (2, 8, 8, 384),
    (2, 8, 8, 384), (2, 8, 8, 64), (2, 8, 8, 384), (2, 8, 8, 384),
    (2, 8, 8, 64), (2, 8, 8, 384), (2, 8, 8, 384), (2, 8, 8, 64),
    (2, 8, 8, 384), (2, 8, 8, 384), (2, 8, 8, 96), (2, 8, 8, 576),
    (2, 8, 8, 576), (2, 8, 8, 96), (2, 8, 8, 576), (2, 8, 8, 576),
    (2, 8, 8, 96), (2, 8, 8, 576), (2, 4, 4, 576), (2, 4, 4, 160),
    (2, 4, 4, 960), (2, 4, 4, 960), (2, 4, 4, 160), (2, 4, 4, 960),
    (2, 4, 4, 960), (2, 4, 4, 160), (2, 4, 4, 960), (2, 4, 4, 960),
    (2, 4, 4, 320), (2, 4, 4, 1280)
]

moblenet_v2_expected_feature_map_shape_128_explicit_padding = [
    (2, 64, 64, 32), (2, 64, 64, 96), (2, 32, 32, 96), (2, 32, 32, 24),
    (2, 32, 32, 144), (2, 32, 32, 144), (2, 32, 32, 24), (2, 32, 32, 144),
    (2, 16, 16, 144), (2, 16, 16, 32), (2, 16, 16, 192), (2, 16, 16, 192),
    (2, 16, 16, 32), (2, 16, 16, 192), (2, 16, 16, 192), (2, 16, 16, 32),
    (2, 16, 16, 192), (2, 8, 8, 192), (2, 8, 8, 64), (2, 8, 8, 384),
    (2, 8, 8, 384), (2, 8, 8, 64), (2, 8, 8, 384), (2, 8, 8, 384),
    (2, 8, 8, 64), (2, 8, 8, 384), (2, 8, 8, 384), (2, 8, 8, 64),
    (2, 8, 8, 384), (2, 8, 8, 384), (2, 8, 8, 96), (2, 8, 8, 576),
    (2, 8, 8, 576), (2, 8, 8, 96), (2, 8, 8, 576), (2, 8, 8, 576),
    (2, 8, 8, 96), (2, 8, 8, 576), (2, 4, 4, 576), (2, 4, 4, 160),
    (2, 4, 4, 960), (2, 4, 4, 960), (2, 4, 4, 160), (2, 4, 4, 960),
    (2, 4, 4, 960), (2, 4, 4, 160), (2, 4, 4, 960), (2, 4, 4, 960),
    (2, 4, 4, 320), (2, 4, 4, 1280)
]

mobilenet_v2_expected_feature_map_shape_with_dynamic_inputs = [
    (2, 64, 64, 32), (2, 64, 64, 96), (2, 32, 32, 96), (2, 32, 32, 24),
    (2, 32, 32, 144), (2, 32, 32, 144), (2, 32, 32, 24), (2, 32, 32, 144),
    (2, 16, 16, 144), (2, 16, 16, 32), (2, 16, 16, 192), (2, 16, 16, 192),
    (2, 16, 16, 32), (2, 16, 16, 192), (2, 16, 16, 192), (2, 16, 16, 32),
    (2, 16, 16, 192), (2, 8, 8, 192), (2, 8, 8, 64), (2, 8, 8, 384),
    (2, 8, 8, 384), (2, 8, 8, 64), (2, 8, 8, 384), (2, 8, 8, 384),
    (2, 8, 8, 64), (2, 8, 8, 384), (2, 8, 8, 384), (2, 8, 8, 64),
    (2, 8, 8, 384), (2, 8, 8, 384), (2, 8, 8, 96), (2, 8, 8, 576),
    (2, 8, 8, 576), (2, 8, 8, 96), (2, 8, 8, 576), (2, 8, 8, 576),
    (2, 8, 8, 96), (2, 8, 8, 576), (2, 4, 4, 576), (2, 4, 4, 160),
    (2, 4, 4, 960), (2, 4, 4, 960), (2, 4, 4, 160), (2, 4, 4, 960),
    (2, 4, 4, 960), (2, 4, 4, 160), (2, 4, 4, 960), (2, 4, 4, 960),
    (2, 4, 4, 320), (2, 4, 4, 1280)
]

moblenet_v2_expected_feature_map_shape_299 = [
    (2, 150, 150, 32), (2, 150, 150, 96), (2, 75, 75, 96), (2, 75, 75, 24),
    (2, 75, 75, 144), (2, 75, 75, 144), (2, 75, 75, 24), (2, 75, 75, 144),
    (2, 38, 38, 144), (2, 38, 38, 32), (2, 38, 38, 192), (2, 38, 38, 192),
    (2, 38, 38, 32), (2, 38, 38, 192), (2, 38, 38, 192), (2, 38, 38, 32),
    (2, 38, 38, 192), (2, 19, 19, 192), (2, 19, 19, 64), (2, 19, 19, 384),
    (2, 19, 19, 384), (2, 19, 19, 64), (2, 19, 19, 384), (2, 19, 19, 384),
    (2, 19, 19, 64), (2, 19, 19, 384), (2, 19, 19, 384), (2, 19, 19, 64),
    (2, 19, 19, 384), (2, 19, 19, 384), (2, 19, 19, 96), (2, 19, 19, 576),
    (2, 19, 19, 576), (2, 19, 19, 96), (2, 19, 19, 576), (2, 19, 19, 576),
    (2, 19, 19, 96), (2, 19, 19, 576), (2, 10, 10, 576), (2, 10, 10, 160),
    (2, 10, 10, 960), (2, 10, 10, 960), (2, 10, 10, 160), (2, 10, 10, 960),
    (2, 10, 10, 960), (2, 10, 10, 160), (2, 10, 10, 960), (2, 10, 10, 960),
    (2, 10, 10, 320), (2, 10, 10, 1280)
]

moblenet_v2_expected_feature_map_shape_enforcing_min_depth = [
    (2, 150, 150, 32), (2, 150, 150, 192), (2, 75, 75, 192), (2, 75, 75, 32),
    (2, 75, 75, 192), (2, 75, 75, 192), (2, 75, 75, 32), (2, 75, 75, 192),
    (2, 38, 38, 192), (2, 38, 38, 32), (2, 38, 38, 192), (2, 38, 38, 192),
    (2, 38, 38, 32), (2, 38, 38, 192), (2, 38, 38, 192), (2, 38, 38, 32),
    (2, 38, 38, 192), (2, 19, 19, 192), (2, 19, 19, 32), (2, 19, 19, 192),
    (2, 19, 19, 192), (2, 19, 19, 32), (2, 19, 19, 192), (2, 19, 19, 192),
    (2, 19, 19, 32), (2, 19, 19, 192), (2, 19, 19, 192), (2, 19, 19, 32),
    (2, 19, 19, 192), (2, 19, 19, 192), (2, 19, 19, 32), (2, 19, 19, 192),
    (2, 19, 19, 192), (2, 19, 19, 32), (2, 19, 19, 192), (2, 19, 19, 192),
    (2, 19, 19, 32), (2, 19, 19, 192), (2, 10, 10, 192), (2, 10, 10, 32),
    (2, 10, 10, 192), (2, 10, 10, 192), (2, 10, 10, 32), (2, 10, 10, 192),
    (2, 10, 10, 192), (2, 10, 10, 32), (2, 10, 10, 192), (2, 10, 10, 192),
    (2, 10, 10, 32), (2, 10, 10, 32)
]

moblenet_v2_expected_feature_map_shape_with_conv_defs = [
    (2, 150, 150, 32), (2, 150, 150, 96), (2, 75, 75, 96), (2, 75, 75, 24),
    (2, 75, 75, 144), (2, 75, 75, 144), (2, 75, 75, 24), (2, 75, 75, 144),
    (2, 38, 38, 144), (2, 38, 38, 32), (2, 38, 38, 192), (2, 38, 38, 192),
    (2, 38, 38, 32), (2, 38, 38, 192), (2, 38, 38, 192), (2, 38, 38, 32),
    (2, 38, 38, 192), (2, 19, 19, 192), (2, 19, 19, 64), (2, 19, 19, 384),
    (2, 19, 19, 384), (2, 19, 19, 64), (2, 19, 19, 384), (2, 19, 19, 384),
    (2, 19, 19, 64), (2, 19, 19, 384), (2, 19, 19, 384), (2, 19, 19, 64),
    (2, 19, 19, 384), (2, 19, 19, 384), (2, 19, 19, 96), (2, 19, 19, 576),
    (2, 19, 19, 576), (2, 19, 19, 96), (2, 19, 19, 576), (2, 19, 19, 576),
    (2, 19, 19, 96), (2, 19, 19, 576), (2, 10, 10, 576), (2, 10, 10, 160),
    (2, 10, 10, 960), (2, 10, 10, 960), (2, 10, 10, 160), (2, 10, 10, 960),
    (2, 10, 10, 960), (2, 10, 10, 160), (2, 10, 10, 960), (2, 10, 10, 960),
    (2, 10, 10, 320), (2, 10, 10, 256)
]
