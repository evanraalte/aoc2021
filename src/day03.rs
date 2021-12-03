use transpose;

static INPUT: &str = include_str!("../assets/day03.txt");


pub fn get_power_consumption(report: &str) -> i32 {
    let width: usize = report.lines().count();
    let height: usize = report.lines().next().unwrap().len();
    let inp: Vec<char>  = report.lines().flat_map(|s| s.chars().collect::<Vec<_>>()).collect();
    println!("{:?}", inp);
    let mut out: Vec<char> = vec!['0'; inp.len()];
    transpose::transpose(&inp, &mut out, width, height);
    println!("{:?}", out);


    let ones: Vec<usize> = out.chunks(width).map(|chunk| chunk.iter().filter(|&c| *c == '1').count()).collect();
    
    let gamma: String = ones.iter().map(|n| if *n > width - *n {'1'} else {'0'}).collect();
    println!("{:?}", ones);
    println!("{:?}", width);
    println!("{:?}", height);
    println!("{:?}", gamma);
    // }
    // .map(|line|  line.filter('1').count())
// isize::from_str_radix(,2).unwrap());
    0
}



pub fn part_a() -> String {
    get_power_consumption(INPUT).to_string()
}
// pub fn part_b() -> String {
//     let mut submarine = Submarine::new();
//     submarine.run_instructions_b(INPUT);
//     submarine.multiply_position().to_string()
// }

#[cfg(test)]
mod tests {
    use super::*;
    static EXAMPLE_INPUT: &str = "00100\n11110\n10110\n10111\n10101\n01111\n00111\n11100\n10000\n11001\n00010\n01010";
    #[test]
    // fn example_a() {
    //     assert_eq!(get_power_consumption(EXAMPLE_INPUT), 198); 
    // }
    fn example_a() {
        assert_eq!(get_power_consumption("00100\n11110"), 198); 
    }

    // #[test]
    // fn example_b() {
    //     let mut submarine = Submarine::new();
    //     submarine.run_instructions_b(EXAMPLE_INPUT);
    //     assert_eq!(submarine.multiply_position(), 900);
    // }
}
