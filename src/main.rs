#[macro_use]
extern crate nom;
use std::env;
mod day01;
mod day02;
mod day03;

fn main() {
    // let args: Vec<String> = env::args().collect();
    // let day = &args[1];
    // let result = match &day[..] {
    //     "day01a" => day01::part_a(),
    //     "day01b" => day01::part_b(),
    //     "day02a" => day02::part_a(),
    //     "day02b" => day02::part_b(),
    //     "day03a" => day03::part_a(),
    //     _ => panic!("Invalid day"),
    // };
    // println!("{:?}", result);
    let inp = vec!['0', '0', '1', '0', '0', '1', '1', '1', '1', '0'];
    let after = vec!['0', '1', '0', '1', '1', '0', '0', '1', '1', '0'];
    let mut out = vec!['0', 10];
    transpose::transpose(&inp, &mut out, 5, 2);
    assert_eq!(output_array, expected_array);
}
