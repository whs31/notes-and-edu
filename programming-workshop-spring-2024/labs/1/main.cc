/*
 * Лабораторная работа 1
 * Студент: Рязанцев Дмитрий
 */

#include <cmath>
#include <concepts>
#include <iostream>
#include <format>

namespace terminal::colors {
  using namespace std::literals;
  auto constexpr red = "\x1b[31m"sv;
  auto constexpr reset = "\x1b[0m"sv;
}

namespace {
  template<std::floating_point T>
  constexpr auto fn(T const x, T const alpha) -> T {
    auto const delta = x - alpha;
    return 1.0 / std::sqrt(std::asin(x - alpha));
  }

  template <typename... Args>
  requires (sizeof...(Args) > 0) and (sizeof...(Args) <= 4)
  auto print_header(std::ostream& stream, Args&&... args) -> void {
    stream << std::format("|{:^10}|{:^10}|{:^10}|{:^10}|\n", std::forward<Args>(args)...);
    stream << std::format("|{:->10}|{:->10}|{:->10}|{:->10}|\n", '-', '-', '-', '-');
  }

  template <typename... Args>
  requires (sizeof...(Args) > 0) and (sizeof...(Args) <= 4)
  auto print_row(std::ostream& stream, Args&&... args) -> void {
    stream << std::format("|{:>10}|{:>10}|{:>10}|{:>10}|\n", std::forward<Args>(args)...);
  }

  auto print_error_and_exit(std::ostream& stream, std::string const& message) -> void {
    ::print_header(stream, "N", "x", "a", "y");
    stream << std::format("|{}{:^43}{}|\n", terminal::colors::red, message, terminal::colors::reset);
    std::exit(1);
  }
}

auto main() -> int {
  auto constexpr X_MIN = -8.5f;
  auto constexpr X_MAX = 26.5f;
  auto constexpr DX = 3.5f;

  std::cout << "Enter value a:\n";
  auto buf = std::string();
  std::cin >> buf;
  auto alpha = 0.0f;
  try {
    alpha = std::stof(buf);
  } catch(std::invalid_argument const&) {
    ::print_error_and_exit(std::cerr, "a must be a valid number");
  }
  if(alpha > 10e6f or alpha < -10e6f)
    ::print_error_and_exit(std::cerr, "a must be in range [-10e6, 10e6]");
  ::print_header(std::cout, "N", "x", "a", "y");
  auto i = 1;
  for(auto x = X_MIN; x <= X_MAX; x += DX) { // NOLINT(*-flp30-c)
    auto const result = ::fn(x, alpha);
    ::print_row(std::cout,
      ++i,
      x,
      alpha,
      std::isnan(result) ? std::format("  -  ") : std::format("{:.2f}", result)
    );
  }
  return 0;
}