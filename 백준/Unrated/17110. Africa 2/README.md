# [Unrated] Africa 2 - 17110 

[문제 링크](https://www.acmicpc.net/problem/17110) 

### 성능 요약

메모리: 31120 KB, 시간: 32 ms

### 분류

분류 없음

### 제출 일자

2024년 11월 10일 23:45:42

### 문제 설명

<p dir="ltr">구데기컵 2018의 첫 번째 문제였던 Africa는 첫 문제답게 문제를 잘 읽기만 하면 정답을 받을 수 있는 쉬운 문제였다. 문제에 적힌 조건을 모두 파악한 브라이언은 바로 코드를 짰고, 예제 입력을 넣었을 때 예제 출력과 같은 결과가 나오는 것을 보고 바로 제출했으나, '틀렸습니다'를 받았다.<br>
자신의 코드가 틀릴 리 없다고 생각했던 브라이언은 채점 시스템에 문제가 있을 것이라 확신하고 같은 코드를 여러 번 제출했으나, 결과는 바뀌지 않았다. 결국 그는 '맞왜틀'을 외치며 출제자에게 항의를 했고, 출제자에게서 문제에는 오류가 없다는 (예상 가능한) 답변을 받았다. 친절한 출제자는 불필요한 정보를 추가로 알려줬는데, 전체 테스트 케이스 중 정확히 절반에 대해서만 정답을 출력하고 나머지 절반은 오답을 출력한다는 것이다. 그리고 여러 번 채점해도 각 테스트 케이스에 대한 결과는 바뀌지 않았다고 한다.<br>
이 이야기를 들은 당신은 과연 어떤 코드를 제출했길래 이런 아름다운 상황이 발생하게 되었는지 궁금해졌다. 그 코드를 재현할 수 있겠는가?<br>
당신의 프로그램은 다음을 모두 만족해야 한다.<br>
- 예제 입력을 넣을 경우 '맞았습니다!!'를 받을 수 있어야 한다.<br>
- 전체 채점 데이터 중 정확히 절반은 정답, 나머지 절반은 오답이어야 한다. 이때 오답은 출력 결과가 정답과 다름을 의미하며 시간 초과 등이 발생하면 안 된다.<br>
- 같은 입력에 대해서는 항상 같은 출력이 나와야 한다. 즉, 랜덤 함수 등을 사용하면 안 된다.<br>
- 채점 데이터는 Africa 채점에 사용되고 있거나 곧 사용될 것과 같다. 채점 데이터의 수는 짝수임이 보장된다.<br>
채점 결과는 다음과 같다.<br>
- 전체 데이터의 수를 2n이라고 할 때, 맞은 테스트 케이스의 수가 n±k인 경우 점수는 100-k점이 되며, 100점이면서 위에 언급한 조건을 모두 만족하면 정답이다.</p>

### 입력 

 <p>첫 줄의 입력 데이터의 개수 <em>N</em> (1 ≤ <em>N</em> ≤ 8)이 입력된다.</p>

<p>다음 <em>N</em>줄에 걸쳐 한 줄에 하나씩 단어가 입력되며, 입력되는 단어는 다음의 8개 중 하나이며, 같은 단어가 두 번 이상 입력되는 경우는 없다. botswana, ethiopia, kenya, namibia, south-africa, tanzania, zambia, zimbabwe</p>

### 출력 

 <p>문제에 해당하는 답을 출력한다. 문제 해결에 필요한 모든 정보는 이 문제에서 제시되는 것을 기준으로 한다.</p>

