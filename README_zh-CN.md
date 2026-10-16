# 更低成本的 varg SDK API素材方案

<!-- TOAPIS-MODEL-COST-UPDATE-20261016 -->
## 模型类型、测试档位与花费

更新：2026-10-16。下表为已验证案例的历史档位与价格；本段补充不改变下方原批次记录。

| 模型（API ID） | 类型 | 测试档位 | 单次报价 | 已确认单次消费 | 数量 |
|---|---|---|---:|---:|---:|
| gpt-image-2(VIP) (`gpt-image-2-vip`) | 图片 | low / 1K / n=1 | $0.0019/image | $0.0019 | 1 |
| gpt-image-2.5-flare | 图片 | high / 1K / n=1 | $0.0225/image | $0.0225 | 1 |
| Nano Banana 2.1 (`gemini-nano-banana-2.1`) | 图片 | 1K / n=1 | $0.015/image | $0.015 | 1 |
| MiniMax H3 (`MiniMax-H3`) | 视频 / 图生视频 | I2V / 5s / 768p / 1:1 | $0.4/clip | $0.4 | 1 |

原图片/视频案例已核对消费小计：**$0.4394**。

独立API素材已验证；上游原生注册、UI和完整工作流尚未验收。

gpt-image-2(VIP) **$0.0019/image 起**；本表 low/1K 实测档位为 **$0.0019/image**。不同模型、质量和分辨率不代表同质效果。

[视频补测、参数、费用与复用](video_extra/README_zh-CN.md)
<!-- /TOAPIS-MODEL-COST-UPDATE-20261016 -->

[English](README.md) · [中文](README_zh-CN.md)

用代码调用模型，再把素材编成视频。

2026-10-16：3张真实图片、1段真实视频；本批成功素材实扣 **$0.4394（87.88积分）**，已按后台导出逐任务核对。

[ToAPIs · 对应模型价格与接入](https://go2v.toapis.com/vg16gc)

## 案例

![varg SDK image examples](screenshots/cn/01-image-cases.png)

[![varg SDK video](screenshots/cn/02-video-case.png)](https://raw.githubusercontent.com/ToAPIs-2025/lower-cost-varg-sdk-toapis/main/demo/first-frame-motion.mp4)

[播放/下载本次5秒视频](https://raw.githubusercontent.com/ToAPIs-2025/lower-cost-varg-sdk-toapis/main/demo/first-frame-motion.mp4) · [MP4](demo/first-frame-motion.mp4)

## 本次模型与花费

| Model | Preset | Catalog estimate / output | Settled charge |
|---|---|---:|---|
| gpt-image-2(VIP) | low / 1K | $0.0019 | $0.0019 |
| gpt-image-2.5-flare | high / 1K | $0.0225 | $0.0225 |
| Nano Banana 2.1 | 1K | $0.015 | $0.015 |
| MiniMax H3 | 5s / 768p / first-frame | $0.40 ($0.08/s) | $0.4 |

对应配置的价表与本次实扣一致；实扣来自后台导出，1积分=$0.005。不同模型/画质不表示同等质量。逐任务记录和原始文件见evidence与examples。

## 怎么运行

```bash
python -m pip install -r requirements.txt
python run_case.py --job jobs/gpt-image-2-vip.json
# Set TOAPIS_API_KEY privately in your local environment first.
python run_case.py --job jobs/gpt-image-2-vip.json --live
python run_case.py --job jobs/video.json --live
```

默认只演练、不扣费。实际执行必须显式加--live；同一run_id保留任务记录，未知提交不自动重发。不要提交.env、Key或私有任务状态。

## 接入原项目

[项目对应接入说明](integration/README_zh-CN.md) · [API contract](integration/toapis-contract.json)

[varg SDK upstream](https://github.com/vargHQ/sdk) · SHA `c26974440bcdb37b42e13696cf58d3d17a636d6d`

这是ToAPIs原创、独立的素材/API示例，不是原项目官方版本或已验收原生Provider。完整上游UI、原生注册和全流程仍需维护者验收；公开包不包含上游源码。
