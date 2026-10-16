# varg SDK integration notes

This is an independent API asset example and integration contract. It is not an official upstream provider, and the contract JSON is not a validated upstream settings import. API output validation is separate from in-app acceptance.

Pinned upstream SHA: c26974440bcdb37b42e13696cf58d3d17a636d6d

- [src/ai-sdk/providers/openai.ts](https://github.com/vargHQ/sdk/blob/c26974440bcdb37b42e13696cf58d3d17a636d6d/src/ai-sdk/providers/openai.ts)
- [src/ai-sdk/video-model.ts](https://github.com/vargHQ/sdk/blob/c26974440bcdb37b42e13696cf58d3d17a636d6d/src/ai-sdk/video-model.ts)
- [src/ai-sdk/generate-video.ts](https://github.com/vargHQ/sdk/blob/c26974440bcdb37b42e13696cf58d3d17a636d6d/src/ai-sdk/generate-video.ts)

Images: authenticate with Bearer, submit once and persist the id, poll the image generations/{id} route, and download result.data[0].url. Resolution fields differ by model; changing Base URL alone is insufficient.

Video: MiniMax-H3, 5s/768p, first frame via image_with_roles, separate videos/generations submit/poll routes. A task id alone is not a successful clip: validate completion, a playable file, and settled billing.

In-app checklist: model selection → duplicate-safe submission → task recovery → save originals → import/display in the original UI → reconcile billing. Full upstream UI acceptance remains pending.
