import json

import requests

POSSIBLE_URLS = {
    "https://arxiv.org": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/ArXiv_web.svg/1200px-ArXiv_web.svg.png",
    "https://www.pnas.org": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/PNAS-logo-primary-2c.png/800px-PNAS-logo-primary-2c.png",
    "https://www.nature.com": "data:image/png;base64,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",
    "https://www.sciencedirect.com": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRa97O7H6L3hHrXoWDOEKI0Fj3uXAkpYh9cSA&usqp=CAU",
    "https://openreview.net": "https://openreview.net/images/openreview_logo_512.png",
    "https://proceedings.neurips.cc": "https://z-images.s3.amazonaws.com/thumb/0/08/Logo_for_Conference_on_Neural_Information_Processing_Systems.svg/200px-Logo_for_Conference_on_Neural_Information_Processing_Systems.svg.png",
    "https://proceedings.mlr.press": "https://avatars.githubusercontent.com/u/12442776?s=200&v=4",
    "https://openaccess.thecvf.com": "https://www.cogrob.org/wp-content/uploads/2020/02/cvpr_logo-610x380.png",
    "https://pubmed.ncbi.nlm.nih.gov": "https://cdn.ncbi.nlm.nih.gov/pubmed/persistent/pubmed-meta-image.png",
    "https://ieeexplore.ieee.org": "data:image/png;base64,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",
}


def url_filter(url):

    if url is None:
        return False

    else:
        for possible_url in POSSIBLE_URLS.keys():
            if url.startswith(possible_url):
                return True
        return False


def papers_to_json(df):

    """
    Take organized dataframe
    """

    df = df.sample(5)

    def _parse(data):
        if data is None:
            return ""
        elif isinstance(data, list):
            return data[0]
        else:
            return data

    def get_logo(url):

        if isinstance(url, list):
            url = url[0]

        for possible_url in POSSIBLE_URLS.keys():
            if url.startswith(possible_url):
                return POSSIBLE_URLS[possible_url]

        return POSSIBLE_URLS["https://arxiv.org"]

    contents = [
        {
            "title": _parse(data[-2]),
            "image_url": get_logo(_parse(data[-3])),
            "description": _parse(data[4]),
            "link": {
                "web_url": _parse(data[-3]),
            },
        }
        for data in df.values
    ]

    post = {
        "object_type": "list",
        "header_title": "Please Read 🧻",
        "header_link": {"web_url": "https://arxiv.org"},
        "contents": contents,
    }
    return post


KAKAO_TOKEN = "v8AvbpCNgiJf0Ws_BG0sjJJRkms3zjRXmv4CXgopb9UAAAGAsu9jHw"  # 주기적으로 업데이트해줘야함


def _send_message(post, KAKAO_TOKEN):
    header = {"Authorization": "Bearer " + KAKAO_TOKEN}

    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"  # 나에게 보내기 주소
    data = {"template_object": json.dumps(post)}
    return requests.post(url, headers=header, data=data)


def send_message(df, KAKAO_TOKEN):

    df = df[df["URL"].apply(url_filter)]
    post = papers_to_json(df)

    result = _send_message(post, KAKAO_TOKEN)
    print(result.text)
