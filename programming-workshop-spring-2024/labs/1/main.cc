/*
 * Лабораторная работа 1
 * Студент: Рязанцев Дмитрий
 */

#include <cmath>
#include <concepts>
#include <iostream>
#include <format>

namespace
{
  template<std::floating_point T>
  constexpr auto fn(T const x, T const alpha) -> T
  {
    using std::sqrt;
    using std::asin;

    auto const delta = x - alpha;
    return 1.0 / sqrt(asin(x - alpha));
  }
}

auto main() -> int
{
  using std::string;
  using std::cin;
  using std::cout;
  using std::cerr;
  using std::endl;

  auto constexpr X_MIN = -8.5f;
  auto constexpr X_MAX = 26.5f;
  auto constexpr DX = 3.5f;

  cout << "Enter value a:\n";
  auto buf = string();
  cin >> buf;
  auto alpha = 0.0f;
  try {
    alpha = std::stof(buf);
  } catch(std::invalid_argument const&) {
    cerr << std::format("Incorrect value of a ({})\n", buf);
    cin.get();
    return 1;
  }
  if(alpha > 10e6f or alpha < -10e6f) {
    cerr << std::format("Incorrect value of a ({})\n", buf);
    cin.get();
    return 1;
  }

  cout << std::format("|  N  |  x  |  a  |  y  |\n");
  cout << std::format("|-----|-----|-----|-----|\n");
  auto i = 1;
  for(auto x = X_MIN; x <= X_MAX; x += DX) { // NOLINT(*-flp30-c)
    auto const result = ::fn(x, alpha);
    cout << std::format("|{:>5}|{:>5}|{:>5}|{:>5}|\n",
      i++,
      x,
      alpha,
      std::isnan(result) ? std::format("  -  ") : std::format("{:.2f}", result)
    );
  }
  return 0;
}