/*
 * Лабораторная работа 4
 * Студент: Рязанцев Дмитрий
 */

#include <cmath>
#include <array>
#include <iostream>
#include <format>
#include <numbers>

using f64 = double;

namespace terminal::colors
{
  using namespace std::literals;

  auto constexpr bold = "\x1b[1m"sv;
  auto constexpr red = "\x1b[31m"sv;
  auto constexpr magenta = "\x1b[35m"sv;
  auto constexpr blue = "\x1b[34m"sv;
  auto constexpr green = "\x1b[32m"sv;
  auto constexpr reset = "\x1b[0m"sv;
}

namespace
{
  using std::numbers::pi;

  [[nodiscard]] auto fn_a(f64 const x) -> f64 { return pi * x; }
  [[nodiscard]] auto fn_b(f64 const x, f64 const epsilon) -> f64 {
    using std::numeric_limits;

    return 1 / (pi * x) + 2 * x / pi * [x, epsilon]() -> f64 {
      auto expr = [x](auto const i) -> f64 { return 1 / (x * x - i * i); };
      auto prev = 0.0;
      auto sum = 0.0;
      for(auto i = 1.0; true; i += 1.0) { // NOLINT(*-flp30-c)
        auto const current = expr(i);
        if(std::abs(prev - current) < epsilon)
          return sum;
        prev = current;
        sum += current;
      }
      return 0.0;
    }();
  }

  [[nodiscard]] auto delta(f64 const a, f64 const b) -> f64 {
    using std::sqrt;
    using std::abs;

    return sqrt(abs(a * a - b * b));
  }
}

auto main() -> int
{
  using std::cin;
  using std::cout;
  using std::cerr;
  using std::endl;
  using std::format;

  auto receive_f64 = [](std::string_view const name) -> f64 {
    f64 result;
    cout << format("Please, enter variable {}{}{}{}:\n",
      terminal::colors::blue,
      terminal::colors::bold,
      name,
      terminal::colors::reset
    );
    if(cin >> result)
      return result;
    else {
      cerr << format("{}Wrong input: {}{}\n",
        terminal::colors::red,
        name,
        terminal::colors::reset
      );
      std::exit(1);
    }
  };

  auto const x_start = receive_f64("X (start)");
  auto const x_end = receive_f64("X (end)");
  auto const x_delta = receive_f64("Delta");

  cout << format("Result table (1){}:\n", terminal::colors::blue);
  cout << format("|    x    |    f(x)    |    F(x)    |   delta   |\n");
  cout << format("|---------|------------|------------|-----------|\n");
  for(auto x = x_start; x <= x_end; x += x_delta) { // NOLINT(*-flp30-c)
    cout << format("|{:<9.2}|{:<12.5}|{:<12.5}|{:<11.5}|\n",
      x,
      ::fn_a(x),
      ::fn_b(x, std::numeric_limits<float>::epsilon() * 2.0),
      ::delta(::fn_a(x), ::fn_b(x, std::numeric_limits<float>::epsilon() * 2.0))
    );
  }
  cout << format("|---------|------------|------------|-----------|{}\n\n",
    terminal::colors::reset
  );

  auto constexpr epsilons = std::array{ 1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7 };

  auto const x_ideal = receive_f64("X (ideal)");
  cout << format("Result table (2){}:\n", terminal::colors::magenta);
  cout << format("|   eps   |    f(x)    |    F(x)    |   delta   |\n");
  cout << format("|---------|------------|------------|-----------|\n");
  for(auto const epsilon : epsilons) { // NOLINT(*-flp30-c)
    cout << format("|{:<9.2}|{:<12.5}|{:<12.5}|{:<11.5}|\n",
      epsilon,
      ::fn_a(x_ideal),
      ::fn_b(x_ideal, epsilon),
      ::delta(::fn_a(x_ideal), ::fn_b(x_ideal, epsilon))
    );
  }
  cout << format("|---------|------------|------------|-----------|\n\n");

  cout << format("{}Done.{}\n", terminal::colors::green, terminal::colors::reset);

  cin.get();
  return 0;
}