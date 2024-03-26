extern crate rand;

mod ball {
    use rand::Rng;

    pub struct Ball {
        pub position: [f64; 3],
        pub velocity: [f64; 3],
        pub color: (u8, u8, u8),
        pub radius: f64,
        pub force: [f64; 3],
        pub mass: f64,
        pub path: Vec<[i64; 2]>,
    }

    impl Ball {
        pub fn new(x: f64, y: f64, velocity: [f64; 2]) -> Ball {
            Ball {
                position: [x, y, 0.0],
                lposition: [x-velocity[0], y-velocity[1], 0.0],
                // color: (rand::thread_rng().gen_range(0..255),
                //         rand::thread_rng().gen_range(0..255),
                //         rand::thread_rng().gen_range(0..255)),
                colour :(255,255,255),
                radius: 10.0,
                // path: Vec::new(),
            }
        }

        pub fn update(&mut self, dt: f64) {
            // self.path.push([self.position[0] as i64, self.position[1] as i64]);
            // if self.path.len() > 500 {
            //     self.path.remove(0);
            // }
            self.force = [0.0, 0.0, 0.0];
            self.position[0] += self.position[0]-self.lposition[0];
            self.position[1] += self.position[1]-self.lposition[1];
            self.position[2] += self.position[2]-self.lposition[2];
        }


        pub fn gravity(balls: &mut Vec<Ball>, k: f64) {
            // Gravity calculation (not implemented here)
        }

        pub fn collide_wall(&mut self, normal: [f64; 3], df: f64) {
            // Collision with walls (not implemented here)
        }
    }
}

mod ball_set {
    use crate::ball::Ball;

    pub struct BallSet {
        pub balls: Vec<Ball>,
        pub ke: f64,
        pub grid_size: f64,
        pub grid_dim: (usize, usize),
    }

    impl BallSet {
        pub fn new(balls: Vec<Ball>) -> BallSet {
            BallSet {
                balls,
                ke: 0.0,
                grid_size: 80.0,
                grid_dim: (16, 9),
            }
        }

        pub fn update(&mut self, dt: f64) {
            // Update logic (not implemented here)
        }

        pub fn draw(&self) {
            // Drawing logic (not implemented here)
        }

        pub fn interact(&mut self, p: u32) {
            // Interaction logic (not implemented here)
        }
    }
}

fn main() {
    // Main logic (not implemented here)
}
