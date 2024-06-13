---
title: all_of
tags:
  - cxx
---
### Определения
#### Классический алгоритм
```cpp
template <typename InputIt, typename UnaryPred>
constexpr auto all_of(InputIt first, InputIt last, UnaryPred p) -> bool;
```
%% link to predicate %%
Проверяет, возвращает ли [[../Ограничения типов (C++11)/Предикат|предикат]] $p$ `true` *для всех* элементов в диапазоне $[first, last]$.

Определено в заголовочном файле:
```cpp
#include <algorithm>
```

[![](https://img.shields.io/badge/cppreference-blue?style=for-the-badge&logo=c%2B%2B)](https://en.cppreference.com/w/cpp/algorithm/all_any_none_of)
#### Ниблоид
```cpp
template <
  std::input_iterator I, 
  std::sentinel_for<I> S, 
  typename Proj = std::identity,
  std::indirect_unary_predicate<std::projected<I, Proj>> Pred
>
constexpr auto ranges::all_of(I first, S last, Pred pred, Proj proj = {}) -> bool;
```
Проверяет, возвращает ли предикат $p$ `true` *для всех* элементов в диапазоне $[first, last]$ (после проекции с помощью проекции $proj$).

```cpp
template <
  ranges::input_range R,
  typename Proj = std::identity,
  std::indirect_unary_predicate<std::projected<ranges::iterator_t<R>, Proj>> Pred
>
constexpr auto ranges::all_of(R&& r, Pred pred, Proj proj = {}) -> bool;
```
Аналогично вышеуказанному, но вместо итераторов диапазона $[first, last]$ принимает коллекцию, используя диапазон $[r.begin(), r.end()]$.

Определено в заголовочном файле:
```cpp
#include <algorithm>
```

[![](https://img.shields.io/badge/cppreference-blue?style=for-the-badge&logo=c%2B%2B)](https://en.cppreference.com/w/cpp/algorithm/ranges/all_any_none_of)

### Подробности
#### Возвращаемое значение
`true`, если предикат вернул `true` для каждого элемента в исследуемом диапазоне.

#### Временная сложность
$$O(N)$$
> Как максимум, `std::distance(first, last)`.

#### Исключения
Не выбрасывает исключений.

#### Пример
```cpp
#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <vector>
#include <fmt/format.h>

auto main() -> int {
  auto vec = std::vector<int>(10, 2);
  std::partial_sum(vec.cbegin(), vec.cend(), vec.begin());
  fmt::println("Among the numbers: {}", fmt::join(vec, ", "));
  if(std::all_of(
    vec.cbegin(), 
    vec.cend(), 
    [](int i) -> bool { return i % 2 == 0; })
  )
    fmt::println("All numbers are even");
  if(std::ranges::all_of(vec, [](int i) -> bool { return i % 2 != 0; }))
    fmt::println("All numbers are odd");
  return 0;
}
```

#### Возможная реализация
```cpp
template <typename InputIt, typename UnaryPred>
constexpr auto all_of(InputIt first, InputIt last, UnaryPred p) -> bool {
  return std::find_if_not(first, last, p) == last;
}
```