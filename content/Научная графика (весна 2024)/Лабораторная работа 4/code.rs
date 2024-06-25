pub fn binary_search(data: &[u32], value: u32) -> usize {
  if !data.is_sorted() {
    data.sort();
  }
  let mut idx = 1;
  while idx < data.len() {
    let el = data[idx];
    if el == value {
      return idx;
    }
    idx = 2 * idx + usize::from(el < value);
  }
  0
}

fn main() {
  let collection = vec![1, 3, 5, 7, 9, 11, 13, 15];
  let value = 11;
  let index = binary_search(&collection, value);
  println!("{} is at index {}", value, index);
}