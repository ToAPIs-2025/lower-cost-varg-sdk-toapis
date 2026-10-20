# Lower-cost varg SDK API asset examples


<!-- TOAPIS-MODELS-20261020 -->
## Model support and prices · 2026-10-20

Added standalone API presets: 31 image request templates and 8 video presets. Current-key pricing matches 26 image and 8 video presets; 5 image templates block new paid calls while pricing is unavailable. Native provider/UI/import/render acceptance remains as documented in the original guide below.

| Image model / tested preset | Current preset quote / image | Historical example amount / image | Fee evidence |
|---|---:|---:|---|
| gpt-image-2(VIP)<br><sub>low</sub> | $0.0019/image | **$0.0019/image** | Billing log, phase unknown |
| gpt-image-2.5-flare-vip<br><sub>low</sub> | Current-key quote unavailable | **$0.005272/image**<br><sub>Token-metered; current $/M unavailable. This sample is not a fixed image tariff.</sub> | Task receipt settled |
| nano_banana<br><sub>1K</sub> | $0.012/image | **$0.012/image** | Billing log, phase unknown |
| gemini-nano-banana-2.1<br><sub>1K</sub> | $0.015/image | **$0.015/image** | Billing log, phase unknown |
| gpt-image-2<br><sub>1K</sub> | $0.015/image | **$0.015/image** | Billing log, phase unknown |
| gemini-nano-banana-2.1-vip<br><sub>1K</sub> | $0.02/image | **$0.02/image** | Billing log, phase unknown |
| qwen-image-3.0<br><sub>1K</sub> | Current-key quote unavailable | **$0.021/image** | Billing log, phase unknown |
| gpt-image-2.5-flare<br><sub>high</sub> | $0.0225/image | **$0.0225/image** | Billing log, phase unknown |
| gpt-image-2.5-sunburst<br><sub>high</sub> | $0.0225/image | **$0.0225/image** | Billing log, phase unknown |
| flux-2-pro<br><sub>1K</sub> | $0.025/image | **$0.025/image** | Billing log, phase unknown |
| doubao-seedream-5-0-pro<br><sub>1K</sub> | $0.042857/image | **$0.042856/image** | Billing log, phase unknown |

| Video model | Preset / input | Settled clip charge | File duration | Case USD/s, ascending |
|---|---|---:|---:|---|
| MiniMax-H3-Max-Turbo | 5s / 480P / text-to-video | $0.125/clip | 5.18s | **$0.024131/s**<br><sub>Pricing tariff: $0.025/s</sub> |
| seedance-2-mini | 4s / 480p / first-frame | $0.13338/clip | 4.04s | **$0.033015/s**<br><sub>Pricing tariff: $3.285714/M total tokens</sub> |
| seedance-2-fast | 4s / 480p / text-to-video | $0.214568/clip | 4.04s | **$0.053111/s**<br><sub>Pricing tariff: $5.285714/M total tokens</sub> |
| kling-v3 | 5s / 720p / std / text-to-video | $0.3/clip | 5.04s | **$0.059524/s**<br><sub>Pricing tariff: $0.06/s</sub> |
| MiniMax-H3 | 5s / 768p / text-to-video | $0.32/clip | 5.17s | **$0.061896/s**<br><sub>Pricing tariff: $0.064/s</sub> |
| seedance-2 | 4s / 480p / first-frame | $0.26676/clip | 4.04s | **$0.06603/s**<br><sub>Pricing tariff: $6.571429/M total tokens</sub> |
| kling-3.0-turbo | 4s / 720p / text-to-video | $0.32/clip | 4.04s | **$0.079208/s**<br><sub>Pricing tariff: $0.08/s</sub> |
| seedance-2-5 | 4s / 480p / text-to-video | $0.3883/clip | 4.04s | **$0.096114/s**<br><sub>Pricing tariff: $10/M total tokens</sub> |

Pricing checked 2026-10-20. Image examples are dated 2026-10-17; video examples 2026-10-20. Tables sort by example amount or case USD/s. Presets and input modes differ; this is not a matched-settings quality ranking. Unknown-phase image logs are not confirmed final net settlements. Current quotes and historical amounts are separate. Video charges are billing=settled; case USD/s divides charge by actual file duration, never processing time. Token tariffs appear in small text and do not imply a fixed per-second price.

gpt-image-2(VIP) starts at $0.0019/image; this low/1K preset is $0.0019/image. The standalone sampler has 31 historically successful image request templates and 8 video presets. Current-key pricing matches 26 image and 8 video presets; 5 image templates block new paid submission until an exact price is available.

[Local sampler](toapis-models/README.md) · [Full price table](PRICING.md) · [Original media and fee evidence](https://github.com/ToAPIs-2025/toapis-quickstart/tree/main/tutorials/model-support-2026-10-20)

Original project examples, historical charges and integration instructions follow. Historical amounts are not rewritten as today’s quotes.

<!-- /TOAPIS-MODELS-20261020 -->

<!-- TOAPIS-MODEL-COST-UPDATE-20261016 -->
## Tested model types, presets and costs

Updated October 16, 2026. These are tested historical presets/prices; this addition does not relabel the original batch below.

| Model (API ID) | Type | Tested preset | Unit quote | Confirmed unit charge | Count |
|---|---|---|---:|---:|---:|
| gpt-image-2(VIP) (`gpt-image-2-vip`) | Image | low / 1K / n=1 | $0.0019/image | $0.0019 | 1 |
| gpt-image-2.5-flare | Image | high / 1K / n=1 | $0.0225/image | $0.0225 | 1 |
| Nano Banana 2.1 (`gemini-nano-banana-2.1`) | Image | 1K / n=1 | $0.015/image | $0.015 | 1 |
| MiniMax H3 (`MiniMax-H3`) | Video / I2V | I2V / 5s / 768p / 1:1 | $0.4/clip | $0.4 | 1 |

Confirmed original image/video example subtotal: **$0.4394**.

Independent API assets validated; upstream native registration, UI and complete workflow remain unvalidated.

gpt-image-2(VIP), **from $0.0019/image**; the tested low/1K preset here is **$0.0019/image**. Different models, qualities and resolutions do not imply equivalent results.

[Video additions, parameters, costs and reuse](video_extra/README.md)
<!-- /TOAPIS-MODEL-COST-UPDATE-20261016 -->


[English](README.md) · [中文](README_zh-CN.md)



Generate media and compose videos in code.



October 16, 2026: 3 real images and 1 real video. Confirmed charge for these completed assets: **$0.4394 (87.88 credits)**, reconciled by task ID against the owner-provided dashboard export.



[ToAPIs · model pricing and setup](https://go2v.toapis.com/vg16ge)



## Examples



![varg SDK image examples](screenshots/en/01-image-cases.png)



[![varg SDK video](screenshots/en/02-video-case.png)](https://raw.githubusercontent.com/ToAPIs-2025/lower-cost-varg-sdk-toapis/main/demo/first-frame-motion.mp4)



[Play/download the real 5-second clip](https://raw.githubusercontent.com/ToAPIs-2025/lower-cost-varg-sdk-toapis/main/demo/first-frame-motion.mp4) · [MP4](demo/first-frame-motion.mp4)



## Models and costs in this run



| Model | Preset | Catalog estimate / output | Settled charge |

|---|---|---:|---|

| gpt-image-2(VIP) | low / 1K | $0.0019 | $0.0019 |

| gpt-image-2.5-flare | high / 1K | $0.0225 | $0.0225 |

| Nano Banana 2.1 | 1K | $0.015 | $0.015 |

| MiniMax H3 | 5s / 768p / first-frame | $0.40 ($0.08/s) | $0.4 |



Catalog rates and confirmed charges match for these tested presets. Charges were reconciled against the owner-provided dashboard export at USD 0.005 per credit. Different models/presets do not imply equal quality. See evidence and examples for task records and originals.



## Run it



```bash

python -m pip install -r requirements.txt

python run_case.py --job jobs/gpt-image-2-vip.json

# Set TOAPIS_API_KEY privately in your local environment first.

python run_case.py --job jobs/gpt-image-2-vip.json --live

python run_case.py --job jobs/video.json --live

```



Dry-run by default. --live explicitly enables paid calls. Stable run_id values preserve task receipts; uncertain submissions are not automatically retried. Never commit .env, keys or private task state.



## Integrating with the original project



[Project-specific integration notes](integration/README.md) · [API contract](integration/toapis-contract.json)



[varg SDK upstream](https://github.com/vargHQ/sdk) · SHA `c26974440bcdb37b42e13696cf58d3d17a636d6d`



These are original, independent ToAPIs asset/API examples, not an official upstream release or an accepted native provider. Full upstream UI, native registration and complete workflows still need maintainer acceptance. No upstream source is redistributed.

