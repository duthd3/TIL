# Heap

파이썬에서는 heapq 모듈을 사용해서 최소 힙과 최대 힙을 구할 수 있다.

## 힙(heap)이란?

힙은 우선순위 큐를 위해 만들어진 자료구조로, 완전 이진트리의 일종이다. 여러 값 중 최대/최소 값을 빠르게 찾아내도록 만들어진 반정렬 상태이다. 최대/최소 값을 찾기 위해서 O(n)의 시간이 걸리지만, 힙을 사용하면 O(logN)만큼 소요된다.

## heappush(item)

힙 불변성을 유지하면서, item 값을 heap으로 push 해주는 메소드이다.

## heappop(item)

힙 불변성을 유지하면서 heap에서 가장 작은 항목을 pop 하고 반환해주는 메서드이다. heappop 메소드를 사용할 때 주의해야할 점은, 힙이 비어 있을 때 heappop 메서드를 호출하면 indexError 발생.

## 최소 힙

부모 노드의 키 값이 자식 노드의 키 값보다 작거나 같은 완전 이진 트리이다.

heap 역할을 할 빈 리스트를 선언해주고, heappush 메서드의 매개변수로 해당 리스트와 추가하고자 하는 값을 넣어주면 리스트에 힙 정렬이 되게 원하는 값이 삽입된다.

```python
import heapq

heap = []

for i in range(1, 6):
	heapq.heappush(heap, i)

for i in range(5):
	print(heapq.heappop(heap))
	# 1 2 3 4 5
```

## 최대 힙

부모 노드의 키 값이 자식 노드의 키 값보다 크거나 같은 완전 이진 트리이다.

heapq는 기본적으로 최소힙만 제공한다. 최대 힙을 구현하기 위해서는 추가적인 절차가 필요하다.

```python
import heapq

values = [1, 2, 3, 4, 5]
heap = []
max_heap = []

for value in values:
	heapq.heappush(heap, -value)
print(heap) # -5, -4, -2, -1, -3

for i in range(len(heap)):
	max_heap.append(-heapq.heappop(heap))
print(max_heap) # 5, 4, 3, 2, 1
```
