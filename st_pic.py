import streamlit as st
from aip import AipImageProcess
import base64

APP_ID = '22580981'
API_KEY = 'xFINsVIt9Wq1PlU4m5MpGlou'
SECRET_KEY = '8oUDsdpSowGn4yvCsqcoElW00GEVNSvv'

client = AipImageProcess(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# Using object notation
add_selectbox = st.sidebar.selectbox(
    "选择图像处理功能",
    ("黑白图像上色", "图像风格转换", "人像动漫化")
)


st.title('图像处理信息系统')

# 上传图片并展示
uploaded_file = st.file_uploader("上传一张图片",type='jpg')

col1, col2= st.columns(2)

if uploaded_file is not None:
    # 将传入的文件转为Opencv格式
    image = uploaded_file.read()
    image_base64 = base64.b64encode(image).decode('utf8')

    with col1:
        # 展示图片
        st.image(image, channels="BGR")
        # 保存图片

    if add_selectbox == "人像动漫化":
        # 调用人物动漫化
        image_base64 = client.selfieAnime(image)['image']
    elif add_selectbox == "黑白图像上色":
        image_base64 = client.colourize(image)['image']
    elif add_selectbox == "图像风格转换":
        # 如果有可选参数
        # Using "with" notation
        with st.sidebar:
            add_radio = st.radio(
            "选择一个图像风格",
            ("cartoon","pencil","color_pencil","warm",
            "wave","lavender","mononoke","scream","gothic"))

        options = {}
        options['option'] = add_radio
        image_base64 = client.styleTrans(image,options)['image']
        
    #将图片保存为文件
    #print(image_base64)
    imgdata = base64.b64decode(image_base64)
    with open("test_cartoon.jpg",'wb') as f:
        f.write(imgdata)
    #print(res_image)

if st.button('Run'):
    # 展示图片
    with col2:
        st.image('test_cartoon.jpg', channels="BGR",caption=add_selectbox)
        # 如果按钮点击，则展示
        with open("test_cartoon.jpg", "rb") as file:
            btn = st.download_button(
                    label="下载图片",
                    data=file,
                    file_name="bingbing.png")

