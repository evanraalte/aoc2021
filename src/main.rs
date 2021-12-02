#[macro_use]
extern crate nom;
use std::env;
mod day01;
mod day02;

fn main() {
    let args: Vec<String> = env::args().collect();
    let day = &args[1];
    let result = match &day[..] {
        "day01a" => day01::part_a(),
        "day01b" => day01::part_b(),
        "day02a" => day02::part_a(),
        "day02b" => day02::part_b(),
        _ => panic!("Invalid day"),
    };
    println!("{:?}", result);
}
