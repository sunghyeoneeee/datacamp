from google.colab import drive
drive.mount('/content/drive') # 코랩이랑 드라이브 연결

!unzip -qq '/content/drive/MyDrive/데이터 분석 대회/training.zip' -d 'training' # training 파일 압축 풀기
!unzip -qq '/content/drive/MyDrive/데이터 분석 대회/test.zip' -d 'test' # test 파일 압축 풀기