# varg SDK video additions and model costs

[English](README.md) · [中文](README_zh-CN.md)

Project-specific tested outputs and failed attempts are recorded separately; earlier examples remain intact.

| Model/API ID | Result | Output | Clip cost | USD/second | Cost evidence |
|---|---|---|---:|---:|---|
| Seedance 2.5 (`seedance-2-5`) | HTTP 400 | no successful output | unverified | — | charge unverified, not assumed free |

Requested: 4 seconds, 480p, 1:1, generate_audio=false, one first frame, no video/audio input. Successful outputs are 640×640, 24 fps and 4.04 seconds. Seedance bills total tokens; USD/second divides this clip’s settled cost by actual output duration, not a fixed per-second rate.

This submission returned HTTP 400. A business-ID lookup recovered no task, there is no playable output, and it was not resubmitted. The earlier MiniMax example remains valid. This failure does not establish general model unavailability or a free/cancelled charge.

## Reuse

Run from this tutorial’s root directory:

```sh
python video_extra/run_seedance_example.py --job video_extra/job.json
# One paid task with your private TOAPIS_API_KEY:
python video_extra/run_seedance_example.py --job video_extra/job.json --live
```

Default is dry-run. --live makes one paid task. Preserve .toapis-state; missing IDs and terminal failures never trigger automatic resubmission. Result downloads carry no API key.

[Seedance 2 / 2 Mini API](https://docs.toapis.com/docs/cn/api-reference/videos/seedance-2/generation) · [Seedance 2.5 API](https://docs.toapis.com/docs/cn/api-reference/videos/seedance-2-5/generation)

The historical MiniMax sample is 5s/768p; these Seedance samples are 480p. They do not establish equal-quality pricing or a universal price ranking.
