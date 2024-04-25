/*
 * Лабораторная работа 2
 * Студент: Рязанцев Дмитрий
 */

#include <cmath>
#include <concepts>
#include <iostream>
#include <format>

namespace
{
  [[nodiscard]] constexpr auto sum_of_digits(int const n) -> int { // NOLINT(*-no-recursion)
    return n == 0 ? 0 : n % 10 + sum_of_digits(n / 10);
  }

  [[nodiscard]] constexpr auto sum_of_m_last_digits(int const n, int const m) -> int { // NOLINT(*-no-recursion)
    return m == 0 ? 0 : sum_of_m_last_digits(n / 10, m - 1) + n % 10;
  }

  [[nodiscard]] constexpr auto digits(int const n) -> int { // NOLINT(*-no-recursion)
    return n == 0 ? 0 : 1 + digits(n / 10);
  }

  [[nodiscard]] constexpr auto odd_digits_count(int const n) -> int { // NOLINT(*-no-recursion)
    return n == 0 ? 0 : n % 2 + odd_digits_count(n / 10);
  }

  [[nodiscard]] constexpr auto is_prime(long const n) -> bool
  {
    if(n <= 1)
      return false;
    for(auto i = 2; i * i <= n; ++i)
      if(n % i == 0)
        return false;
    return true;
  }
}

auto main() -> int
{
  using std::string;
  using std::string_view;
  using std::cin;
  using std::cout;
  using std::cerr;
  using std::endl;

  auto read_number_from_terminal = [](string_view const name) -> long
  {
    cout << std::format("Enter {}:\n", name);
    auto buf = string();
    cin >> buf;
    try {
      return std::stoi(buf);
    } catch(std::invalid_argument const&) {
      cerr << std::format("Incorrect value of {} ({})\n", name, buf);
      cin.get();
      return 1;
    }
  };

  auto const m = read_number_from_terminal("M");
  auto const n = read_number_from_terminal("N");
  if(m <= 0 or n <= 0) {
    cerr << "Incorrect values of M and N (must be > 0)\n";
    cin.get();
    return 1;
  }

  cout << std::format("\nSum of digits of {} last digits of {} = {}\n", m, n, ::sum_of_m_last_digits(n, m));
  cout << std::format("Odd digits count of {} = {}\n", n, ::odd_digits_count(n));
  cout << std::format("Even digits count of {} = {}\n", n, ::digits(n) - ::odd_digits_count(n));
  cout << std::format("Is N = {} prime? {}\n", n, ::is_prime(n) ? "Yes" : "No");
  cout << std::format("Is M = {} prime? {}\n", m, ::is_prime(m) ? "Yes" : "No");

  return 0;
}