static INPUT: &str = include_str!("../assets/day07.txt");



pub fn calc_fuel(inp: &str, partb: bool) -> i32 {
    let crabs: Vec<i32> = inp.split(',').map(|n| n.parse().unwrap()).collect();
    
    let f = | n: i32| -> i32 { if partb { (n * (n + 1))/2} else {n}};
    let cost_sum = | p | {crabs.iter().map(|c| f((c - p as i32).abs()) ).sum()};

    let n = *crabs.iter().min().unwrap()..*crabs.iter().max().unwrap();
    let costs = n.map(|p| cost_sum(p)).collect::<Vec<i32>>();
    *costs.iter().min().unwrap()
}

pub fn part_a() -> String {
    calc_fuel(INPUT,false).to_string()
}
pub fn part_b() -> String {
    calc_fuel(INPUT,true).to_string()
}

#[cfg(test)]
mod tests {
    use super::*;
    static SAMPLE_INPUT: &str = include_str!("../assets/day07-sample.txt");
    #[test]
    fn example_a() {
        assert_eq!(calc_fuel(SAMPLE_INPUT,false), 37);
    }

    #[test]
    fn example_b() {
        assert_eq!(calc_fuel(SAMPLE_INPUT,true), 168);
    }
}
