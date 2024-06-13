cmake_minimum_required(VERSION 3.0.0)
project(lab2
  DESCRIPTION "Лабораторная работа 2"
  HOMEPAGE_URL "github.com/whs31/education"
  LANGUAGES CXX
)

set(CMAKE_CXX_STANDARD 20)

add_executable(${PROJECT_NAME})
target_sources(${PROJECT_NAME} PRIVATE main.cc)
target_include_directories(${PROJECT_NAME} PRIVATE ${CMAKE_CURRENT_SOURCE_DIR})