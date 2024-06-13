---
title: all_of
tags:
  - cxx
---
```cpp
template <typename InputIt, typename UnaryPred>
constexpr auto all_of(InputIt first, InputIt last, UnaryPred p) -> bool;
```
Проверяет, возвращает ли предикат $p$ `true` *для всех* элементов в диапазоне $[first, last]$.
