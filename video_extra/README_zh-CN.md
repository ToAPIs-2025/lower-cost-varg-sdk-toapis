# varg SDK 视频补测与模型费用

[English](README.md) · [中文](README_zh-CN.md)

本节仅展示该项目相关的实际测试；原始模型结果和失败记录均保留。

| 模型/API ID | 结果 | 成片 | 单次费用 | 美元/秒 | 费用依据 |
|---|---|---|---:|---:|---|
| Seedance 2.5 (`seedance-2-5`) | HTTP 400 | 无成功输出 | 待确认 | — | 实扣待确认，不认定免费 |

请求参数：4秒、480p、1:1、generate_audio=false、单张首帧，无视频或音频输入。成功输出实际为640×640、24fps、4.04秒。Seedance按总token计费，美元/秒仅为本条已结算费用除以实际成片时长，不是固定秒价。

这次提交返回HTTP 400；按业务ID查询未恢复任务，没有可播放输出，未重复提交。历史MiniMax案例仍有效。本次失败不证明模型普遍不可用，也不证明已被免费取消。

## 复用

在本教程根目录运行：

```sh
python video_extra/run_seedance_example.py --job video_extra/job.json
# One paid task with your private TOAPIS_API_KEY:
python video_extra/run_seedance_example.py --job video_extra/job.json --live
```

默认不调用API；使用--live才发起单条付费任务。保留.toapis-state；未获任务ID或终态失败时不自动重发。URL下载不携带API Key。

[Seedance 2 / 2 Mini API](https://docs.toapis.com/docs/cn/api-reference/videos/seedance-2/generation) · [Seedance 2.5 API](https://docs.toapis.com/docs/cn/api-reference/videos/seedance-2-5/generation)

MiniMax历史样本为5秒/768p，Seedance本节为480p；不能据此断言同画质价格或所有配置的高低。
