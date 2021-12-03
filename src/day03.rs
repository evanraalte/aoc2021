use transpose;

static INPUT: &str = include_str!("../assets/day03.txt");

pub fn get_rating(report: &str, idx: usize) -> usize {
    let num_iterations = report.lines().next().unwrap().len();
    let sub_report = report.to_string();
    for n in 0..num_iterations {
        let gamma_epsilon = get_gamma_epsilon(&sub_report[..]);
        let value = if idx == 0 {
            gamma_epsilon.0
        } else {
            gamma_epsilon.1
        };
        let binary = format!("{:05b}", value);
        println!("binary: {:?}, g/e: {:?}", binary, gamma_epsilon);

        let filter_slice: &str = &binary[0..n + 1].to_string();
        let it = sub_report
            .lines()
            .filter(|line| line.starts_with(filter_slice));

        let sub_report = it.fold(String::new(), |a, b| a + b + "\n");

        println!("<start>");
        for l in sub_report.trim_end().lines() {
            println!("{:?}", l);
        }
        println!("<end>");

        if sub_report.trim_end().lines().count() == 1 || n == num_iterations - 1 {
            let val = usize::from_str_radix(sub_report.trim_end(), 2).unwrap();
            return val;
        }
    }
    return 0;
}

pub fn get_oxygen_generator_rating(report: &str) -> usize {
    get_rating(report, 0)
}

pub fn c02_scrubber_rating(report: &str) -> usize {
    get_rating(report, 1)
}

pub fn get_gamma_epsilon(report: &str) -> (usize, usize) {
    let width: usize = report.lines().count();
    let height: usize = report.lines().next().unwrap().len();
    let inp: Vec<char> = report
        .lines()
        .flat_map(|s| s.chars().collect::<Vec<_>>())
        .collect();

    let mut out: Vec<char> = vec!['0'; inp.len()];
    transpose::transpose(&inp, &mut out, height, width);

    let ones: Vec<usize> = out
        .chunks(width)
        .map(|chunk| chunk.iter().filter(|&c| *c == '1').count())
        .collect();

    let gamma_binary: String = ones
        .iter()
        .map(|n| if *n >= width - *n { '1' } else { '0' })
        .collect();

    let gamma = usize::from_str_radix(gamma_binary.as_str(), 2).unwrap();
    let mask = (1 << height) - 1;
    let epsilon = gamma ^ mask;
    (gamma, epsilon)
}

pub fn get_power_consumption(report: &str) -> usize {
    let (gamma, epsilon) = get_gamma_epsilon(report);
    gamma * epsilon
}

pub fn part_a() -> String {
    get_power_consumption(INPUT).to_string()
}

#[cfg(test)]
mod tests {
    use super::*;
    static EXAMPLE_INPUT: &str =
        "00100\n11110\n10110\n10111\n10101\n01111\n00111\n11100\n10000\n11001\n00010\n01010";
    #[test]
    fn example_a() {
        assert_eq!(get_power_consumption(EXAMPLE_INPUT), 198);
    }

    #[test]
    fn example_b_oxygen_generator_rating() {
        assert_eq!(get_oxygen_generator_rating(EXAMPLE_INPUT), 23);
    }
    #[test]
    fn example_b_c02_scrubber_rating() {
        assert_eq!(c02_scrubber_rating(EXAMPLE_INPUT), 10);
    }
    // #[test]
    // fn example_b() {
    //     let mut submarine = Submarine::new();
    //     submarine.run_instructions_b(EXAMPLE_INPUT);
    //     assert_eq!(submarine.multiply_position(), 900);
    // }
}
