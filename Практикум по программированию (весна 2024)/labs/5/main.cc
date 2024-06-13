/*
 * Лабораторная работа 3
 * Студент: Рязанцев Дмитрий
 */

#include <iostream>
#include <format>
#include <memory>
#include <tuple>
#include <random>

namespace terminal::colors
{
  using namespace std::literals;

  auto constexpr yellow = "\x1b[33m"sv;
  auto constexpr green = "\x1b[32m"sv;
  auto constexpr reset = "\x1b[0m"sv;
}

auto main() -> int
{
  using std::cin;
  using std::cout;
  using std::cerr;
  using std::endl;

  auto const [rows, columns] = []() -> std::tuple<int, int>
  {
    auto r = 0, c = 0;
    cout << "Enter rows count:" << endl;
    cin >> r;
    cout << "\nEnter columns count:" << endl;
    cin >> c;
    if(r <= 0 or c <= 0 or r > 20 or c > 20 or cin.fail()) {
      cerr << "Invalid dimensions" << endl;
      std::exit(1);
    }
    return { r, c };
  }();

  auto rd = std::random_device();
  auto gen = std::mt19937(rd());
  auto distrib = std::uniform_int_distribution<>(0, 100);
  auto matrix = std::make_unique<int[]>(rows * columns);
  for(auto i = 0; i < rows * columns; ++i)
    matrix[i] = distrib(gen);

  auto print_matrix = [&]{
    for(auto i = 0; i < rows; ++i) {
      for(auto j = 0; j < columns; ++j)
        cout << std::format("{:<3} ",matrix[i * columns + j]);
      cout << endl;
    }
  };

  cout << std::format("\n\nInitial matrix of size {}x{}: {}\n", rows, columns, terminal::colors::yellow);
  print_matrix();

  // make all elements above the main diagonal zero
  for(auto i = 0; i < rows; ++i)
    for(auto j = 0; j < columns; ++j)
      if(i < j)
        matrix[i * columns + j] = 0;

  cout << std::format("\n\nMatrix with zeros above the main diagonal: {}\n", terminal::colors::green);
  print_matrix();
  cout << terminal::colors::reset << "\nDone!" << endl;

  return 0;
}