use transpose;

static INPUT: &str = include_str!("../assets/day03.txt");

fn has_more_ones(l: Vec<char>) -> bool {
    l.iter().filter(|&c| *c == '1').count() >= l.iter().filter(|&c| *c == '0').count() 
}

fn get_power_rate(report: &str) -> u32 {
    let width: usize = report.lines().count();
    let height: usize = report.lines().next().unwrap().len();
    let inp: Vec<char> = report
        .lines()
        .flat_map(|s| s.chars().collect::<Vec<_>>())
        .collect();

    let mut out: Vec<char> = vec!['0'; inp.len()];
    transpose::transpose(&inp, &mut out, height, width);

    let mut gamma: u32 = 0;
    let cs = out.chunks(width);
    for line in cs {
        gamma = gamma << 1;
        gamma += has_more_ones(line.to_vec()) as u32;
    }
    let mask = (2 as u32).pow((height) as u32) -1;
    let epsilon = gamma ^ mask;


    return gamma * epsilon
}


pub fn part_a() -> String {
    get_power_rate(INPUT).to_string()
}

#[cfg(test)]
mod tests {
    use super::*;
    static EXAMPLE_INPUT: &str = include_str!("../assets/day03-sample.txt");

    #[test]
    fn example_a() {
        assert_eq!(get_power_rate(EXAMPLE_INPUT), 198);
    }
}
