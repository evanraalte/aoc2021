use nom::{digit, space, IResult};
use std::str::{self, FromStr};

static INPUT: &str = include_str!("../assets/day02.txt");

named!(number(&[u8]) -> usize,
    map_res!(
        map_res!(
            digit,
            str::from_utf8
        ),
        FromStr::from_str
    )
);

#[derive(Debug, PartialEq, Eq)]
pub enum Command {
    Forward,
    Down,
    Up,
}

named!(command(&[u8]) -> Command,
    alt!(
        value!(Command::Forward, tag!("forward")) |
        value!(Command::Down, tag!("down")) |
        value!(Command::Up, tag!("up"))
    )
);

#[derive(Debug, PartialEq, Eq)]
pub struct Instruction {
    command: Command,
    x: i32,
}

named!(instruction(&[u8]) -> Instruction,
    chain!(
        cmd: command ~
        space ~
        x: number ~
        || Instruction { command: cmd, x: x as i32}
    )
);

pub struct Submarine {
    pos_horizontal: i32,
    depth: i32,
    aim: i32,
}

impl Submarine {
    fn new() -> Submarine {
        Submarine {
            pos_horizontal: 0,
            depth: 0,
            aim: 0,
        }
    }
    fn run_instructions_a(&mut self, program: &str) {
        for line in program.lines() {
            match instruction(line.as_bytes()) {
                IResult::Done(rest, ref ins) if rest == [] => match ins.command {
                    Command::Forward => self.pos_horizontal += ins.x,
                    Command::Down => self.depth += ins.x,
                    Command::Up => self.depth -= ins.x,
                },
                _ => panic!("Invalid instruction line: {}", line),
            }
        }
    }
    fn run_instructions_b(&mut self, program: &str) {
        for line in program.lines() {
            match instruction(line.as_bytes()) {
                IResult::Done(rest, ref ins) if rest == [] => match ins.command {
                    Command::Forward => {
                        self.pos_horizontal += ins.x;
                        self.depth += self.aim * ins.x
                    }
                    Command::Down => self.aim += ins.x,
                    Command::Up => self.aim -= ins.x,
                },
                _ => panic!("Invalid instruction line: {}", line),
            }
        }
    }

    fn multiply_position(&self) -> i32 {
        self.pos_horizontal * self.depth
    }
}

pub fn part_a() -> String {
    let mut submarine = Submarine::new();
    submarine.run_instructions_a(INPUT);
    submarine.multiply_position().to_string()
}
pub fn part_b() -> String {
    let mut submarine = Submarine::new();
    submarine.run_instructions_b(INPUT);
    submarine.multiply_position().to_string()
}

#[cfg(test)]
mod tests {
    use super::*;
    static EXAMPLE_INPUT: &str = "forward 5\ndown 5\nforward 8\nup 3\ndown 8\nforward 2";
    #[test]
    fn example_a() {
        let mut submarine = Submarine::new();
        submarine.run_instructions_a(EXAMPLE_INPUT);
        assert_eq!(submarine.multiply_position(), 150);
    }

    #[test]
    fn example_b() {
        let mut submarine = Submarine::new();
        submarine.run_instructions_b(EXAMPLE_INPUT);
        assert_eq!(submarine.multiply_position(), 900);
    }
}
