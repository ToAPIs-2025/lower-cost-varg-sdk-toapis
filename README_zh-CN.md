# 更低成本的 varg SDK API素材方案

[English](README.md) · [中文](README_zh-CN.md)

用代码调用模型，再把素材编成视频。

2026-10-16：3张真实图片、1段真实视频；本批成功素材按价表估算 **$0.4394**，实际扣费待后台核对。

[ToAPIs · 对应模型价格与接入](https://go2v.toapis.com/vg16gc)

## 案例

![varg SDK image examples](screenshots/cn/01-image-cases.png)

[![varg SDK video](screenshots/cn/02-video-case.png)](https://raw.githubusercontent.com/ToAPIs-2025/lower-cost-varg-sdk-toapis/main/demo/first-frame-motion.mp4)

[播放/下载本次5秒视频](https://raw.githubusercontent.com/ToAPIs-2025/lower-cost-varg-sdk-toapis/main/demo/first-frame-motion.mp4) · [MP4](demo/first-frame-motion.mp4)

## 本次模型与花费

| Model | Preset | Catalog estimate / output | Settled charge |
|---|---|---:|---|
| gpt-image-2(VIP) | low / 1K | $0.0019 | 待核对 |
| gpt-image-2.5-flare | high / 1K | $0.0225 | 待核对 |
| Nano Banana 2.1 | 1K | $0.015 | 待核对 |
| MiniMax H3 | 5s / 768p / first-frame | $0.40 ($0.08/s) | 待核对 |

以上是本次明确配置的费率估算，不是已结算金额；不同模型/画质不表示同等质量。每项任务、请求和原始文件见evidence与examples。

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
