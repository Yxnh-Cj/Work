from scraper import Scraper

# 创建 Scraper 实例
scraper = Scraper()

# 用抖音/TikTok分享链接进行解析
video_url = "https://www.douyin.com/video/7625829258859104235?modeFrom="
result = scraper.parse(video_url)

# result 将是一个包含视频信息、无水印下载链接等的字典对象
print(result)