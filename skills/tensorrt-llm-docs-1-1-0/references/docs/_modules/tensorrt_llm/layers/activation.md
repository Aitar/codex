Original URL: https://nvidia.github.io/TensorRT-LLM/1.1.0/_modules/tensorrt_llm/layers/activation.md

* [Module code](../../index.md)
* tensorrt\_llm.layers.activation

# Source code for tensorrt\_llm.layers.activation

```
# SPDX-FileCopyrightText: Copyright (c) 2022-2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from ..functional import softplus, tanh
from ..module import Module

[docs]
class Mish(Module):

[docs]
    def forward(self, input):
        return input * tanh(softplus(input, beta=1.0, threshold=20.0))
```