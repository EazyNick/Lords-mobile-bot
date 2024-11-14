# 자동화 매크로 스크립트(로드모바일 Bot)

이 프로젝트는 Python의 `pyautogui` 및 `win32gui` 라이브러리를 사용하여 PC 화면에서 특정 이미지를 인식하고 클릭하는 자동화 매크로입니다. 주로 블루스택 에뮬레이터 환경에서 특정 이미지 버튼을 자동으로 탐색, 클릭, 스크롤하는 기능을 구현했습니다.

## 목차
- [주요 기능](#주요-기능)
  - [findandclick.py](#findandclickpy)
  - [GreenBox.py](#greenboxpy)
  - [Guild.py](#guildpy)
  - [main.py](#mainpy)
  - [Product.py](#productpy)
  - [Quest.py](#questpy)
  - [Resource.py](#resourcepy)
  - [window.py](#windowpy)
- [사용 방법](#사용-방법)
- [주의 사항](#주의-사항)

## 프로젝트 구조

- `findandclick.py`: 이미지 인식 후 클릭 기능을 제공하는 클래스.
- `GreenBox.py`: 녹색 선물 상자 이미지 인식 및 클릭.
- `Guild.py`: 길드 관련 기능, 길드 창 탐색 및 보상 수령.
- `main.py`: 메인 스크립트, 각 기능을 순차적으로 실행.
- `Product.py`: 군대 훈련, 차원문 등 다양한 생산 관련 기능.
- `Quest.py`: 퀘스트 창 탐색 및 미션 수행.
- `Resource.py`: 자원 수집 자동화.
- `window.py`: 블루스택 창 위치 및 크기 설정.

## 요구 사항

- Python 3.7 이상
- pyautogui
- win32gui (pywin32 설치 필요)
- keyboard
- Windows OS (win32gui 사용)

설치는 다음 명령어를 통해 가능합니다.

```bash
pip install pyautogui pywin32 keyboard
```

# 주요 기능

### findandclick.py
이미지 탐색 및 클릭을 담당하는 `FindandClick` 클래스를 포함합니다.

- `findandClick(png)`: 주어진 이미지 파일(`png`)이 화면에 있을 경우 해당 위치를 클릭합니다.
- `Scroll(PM)`: 지정된 방향으로 스크롤을 수행합니다.

### GreenBox.py
녹색 상자 아이템을 수집하는 자동화 기능을 제공합니다.

- `GreenBoxGet()`: 특정 이미지(`Light Green Box.PNG`, `Get2.PNG`, `Get.PNG`)를 인식하고 클릭하여 상자를 수집합니다.

### Guild.py
길드 보상을 수령하는 자동화 기능을 포함합니다.

- `GuildGet()`: 길드 보상 창을 탐색하여 보상을 수집하며, 여러 단계의 조건문을 통해 보상 아이템을 자동으로 열고 수집합니다.

### main.py
각 모듈의 기능을 순차적으로 실행하여 전체 자동화 흐름을 관리합니다.

- 블루스택 창을 설정 후 `GreenBoxGet`, `GuildGet`, `Quest`, `Resource` 등의 기능을 반복 실행하며 `keyboard` 라이브러리로 'q' 키 입력을 감지하여 종료할 수 있습니다.

### Product.py
게임 내 다양한 자원 및 생산 활동을 자동화합니다.

- `Army()`: 군대 훈련 자동화.
- `dimensionaldoor()`: 차원문 탐색 및 아이템 수집.
- `Arena()`: 경기장 관련 활동 자동화.
- `ReSet()`: 위치 조정 및 초기화 기능.

### Quest.py
퀘스트 창을 탐색하고 일일 퀘스트 등을 수행하는 자동화 기능을 제공합니다.

- `Quest()`: 퀘스트 화면에 들어가 여러 미션을 탐색하고 자동으로 완료합니다.

### Resource.py
자원을 자동으로 수집하는 기능을 포함합니다.

- `Resource()`: 자원 탐색 창을 열고, 식량, 목재 등 자원 아이템을 수집합니다.
- `Resource2()`: 추가 자원 수집 기능.

### window.py
블루스택 창의 위치 및 크기를 설정하여 특정 창을 기준으로 작업을 수행할 수 있도록 합니다.

- `Window`: 창의 위치를 찾아 고정된 크기로 이동합니다.
- `isRealWindow(hWnd)`: 실제 창인지 확인하는 함수.
- `getWindow()`: 블루스택 창을 찾는 기능을 제공하여, 'BlueStacks App Player' 창을 탐색합니다.

# 사용 방법

1. **프로젝트 파일 준비**: 각 Python 파일과 함께 `assets` 폴더에 각종 이미지 파일을 준비합니다.
2. **스크립트 실행**: `main.py`를 실행하여 자동화 작업을 시작합니다.
3. **작업 중지**: `q` 키를 눌러 스크립트를 중지할 수 있습니다.

```bash
python main.py
```

# 주의 사항
1. 이미지 탐지 정확도를 위해 블루스택 창의 크기와 위치를 정확히 설정해야 합니다.
2. 스크립트 실행 중 블루스택 화면이 방해받지 않도록 주의하세요.
3. assets 폴더 내 이미지 파일 경로가 올바르게 설정되어 있는지 확인하십시오.

