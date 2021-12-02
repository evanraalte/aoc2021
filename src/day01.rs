static INPUT: &str = include_str!("../assets/day01.txt");

pub struct Sonar {
    measurements: Vec<u32>,
}

impl Sonar {
    fn new(data: &str) -> Sonar {
        let measurements: Vec<u32> = data
            .lines()
            .map(|line| line.parse::<u32>().unwrap())
            .collect();
        Sonar {
            measurements: measurements,
        }
    }

    fn count_increments(&self, window_size: usize) -> usize {
        let windows = self.measurements.windows(window_size);
        let slice_sums: Vec<u32> = windows.map(|slice| slice.iter().sum()).collect();
        slice_sums
            .windows(2)
            .map(|w| w[1] > w[0])
            .filter(|&n| n)
            .count()
    }
}

pub fn part_a() -> String {
    let sonar = Sonar::new(INPUT);
    sonar.count_increments(1).to_string()
}
pub fn part_b() -> String {
    let sonar = Sonar::new(INPUT);
    sonar.count_increments(3).to_string()
}

#[cfg(test)]
mod tests {
    use super::*;
    static EXAMPLE_INPUT: &str = "199\n200\n208\n210\n200\n207\n240\n269\n260\n263";

    #[test]
    fn example_a() {
        let sonar = Sonar::new(EXAMPLE_INPUT);
        assert_eq!(sonar.count_increments(1), 7);
    }

    #[test]
    fn example_b() {
        let sonar = Sonar::new(EXAMPLE_INPUT);
        assert_eq!(sonar.count_increments(3), 5);
    }
}
