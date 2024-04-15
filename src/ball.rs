
extern crate rand;
extern crate nalgebra;
use std::cmp::{max, min};

// macro_rules! generate_ball_pixel_positions {
//     (radius: $radius:expr) => {{
//         let mut x: Vec<Point> = vec![];
//         for i in 0..($radius - 1) {
//             for j in (i + 1)..$radius {
//                 if i * i + j * j < $radius * $radius {
//                     x.push(Point::new(i as i32, j as i32));
//                     x.push(Point::new(i as i32, -(j as i32)));
//                     x.push(Point::new(-(i as i32), -(j as i32)));
//                     x.push(Point::new(-(i as i32), j as i32));
//                     x.push(Point::new(j as i32, i as i32));
//                     x.push(Point::new(j as i32, -(i as i32)));
//                     x.push(Point::new(-(j as i32), -(i as i32)));
//                     x.push(Point::new(-(j as i32), i as i32));
//                 };
//             }
//         }
//         x
//     }};
// }
// const PIXEL_POSITIONS:Vec<Point> = generate_ball_pixel_positions!(radius:10);

// static  BALL_PIXEL_POSITIONS: Vec<Point> =generate_ball_pixel_positions(10);
pub mod ball {
    use nalgebra::Vector2;
    
    // use rand::Rng;
    use sdl2::pixels::Color;
    use sdl2::rect::Rect;
    use sdl2::render::WindowCanvas;
    use sdl2::rect::Point;
    
    pub struct Ball {
        pub position: Vector2<f64>,
        pub velocity:Vector2<f64>,
        pub color: (u8, u8, u8),
        pub radius: i32,
  
        // pub path: Vec<[i64; 2]>,
    }

    impl Ball {
        pub fn new(x: f64, y: f64, velocity:Vector2<f64>) -> Ball {

            Ball {
                position: Vector2::new(x, y),
                velocity: velocity,
                radius: 10,
                color :(255,255,255),

                // path: Vec::new(),
                // color: (rand::thread_rng().gen_range(0..255),
                //         rand::thread_rng().gen_range(0..255),
                    //         rand::thread_rng().gen_range(0..255)),
                }
            }

        pub fn update(&mut self,dt:f64) {
            // self.path.push([self.position[0] as i64, self.position[1] as i64]);
            // if self.path.len() > 500 {
            //     self.path.remove(0);
            // }
                self.position += self.velocity*dt;
        }   



        pub fn collide(&mut self, other: &mut Ball) {
            let dist: f64= (other.position - self.position).norm();
            if dist < (self.radius+other.radius) as f64 {
                let collision_normal:Vector2<f64> = (self.position-other.position)/dist;
                let relative_velocity =  self.velocity-other.velocity;
                let impulse = collision_normal * relative_velocity.dot(&collision_normal);
                self.velocity-=impulse;
                other.velocity+=impulse;
                self.position += collision_normal * ((self.radius+other.radius) as f64 -dist) * (0.5);
                other.position -= collision_normal * ((self.radius+other.radius) as f64 -dist) * (0.5);
                                    
            }
        }
//         pub fn draw(&self, canvas: &mut WindowCanvas) {
//             let color = Color::RGB(self.color.0, self.color.1, self.color.2);
//             canvas.set_draw_color(color);
//             for i in 0..(self.radius - 1.0 ) as i32 {
//                              for j in (i + 1)..(self.radius-1.0) as i32  {
//                                  if i * i + j * j < (self.radius * self.radius) as i32  {
// canvas.draw_point(Point::new(i as i32, j as i32)).expect("failed to draw circle");
// canvas.draw_point(Point::new(i as i32, -(j as i32))).expect("failed to draw circle");
// canvas.draw_point(Point::new(-(i as i32), -(j as i32))).expect("failed to draw circle");
// canvas.draw_point(Point::new(-(i as i32), j as i32)).expect("failed to draw circle");
// canvas.draw_point(Point::new(j as i32, i as i32)).expect("failed to draw circle");
// canvas.draw_point(Point::new(j as i32, -(i as i32))).expect("failed to draw circle");
// canvas.draw_point(Point::new(-(j as i32), -(i as i32))).expect("failed to draw circle");
// canvas.draw_point(Point::new(-(j as i32), i as i32)).expect("failed to draw circle");

// }}}       }   

//     }
// }
pub fn draw(&self, canvas: &mut WindowCanvas) {
    let color = Color::RGB(self.color.0, self.color.1, self.color.2);
    canvas.set_draw_color(color);

    let radius_squared = (self.radius * self.radius) as i32;

    for x in  0..(self.radius) as i32 {
        for y in 0 ..(self.radius) as i32 {
            let distance_squared = x * x + y * y;
            if distance_squared <= radius_squared {
                canvas.draw_point(Point::new(x + self.position.x as i32, y + self.position.y as i32))
                    .expect("failed to draw circle");
                canvas.draw_point(Point::new(-x + self.position.x as i32, y + self.position.y as i32))
                    .expect("failed to draw circle");
                canvas.draw_point(Point::new(-x + self.position.x as i32,- y + self.position.y as i32))
                .expect("failed to draw circle");
                canvas.draw_point(Point::new(x + self.position.x as i32, -y + self.position.y as i32))
                .expect("failed to draw circle");
                }

        }
    }
}
    // pub fn draw(&self, canvas: &mut WindowCanvas) {
    //     canvas.set_draw_color(Color::RGB(self.color.0, self.color.1, self.color.2));
    //     let center = self.position.map(|x| x as i32);
    //     let radius = self.radius as i32;
    //     let rect = Rect::new(center.x - radius, center.y - radius,( radius * 2 )as u32,( radius * 2 )as u32);
    //     canvas.fill_rect(rect).expect("Failed to draw ball");
    // }   




}
}
fn get_two_elements<T>(vec: &mut Vec<T>, first: usize, second: usize) -> (&mut T, &mut T) {
    let s = max(first, second);
    let f = min(first, second);
    assert!(second < vec.len());
    if let [f, .., s] = &mut vec[f..=s] {
        (f, s)
    } else {
        unreachable!()
    }
}

pub mod ball_set {
    use crate::ball::ball::Ball;

    use sdl2::render::WindowCanvas;
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
                grid_size: 20.0,
                grid_dim: (64, 36),
            }
        }

        pub fn update(&mut self,dt:f64) {
            let mut grid: Vec<Vec<usize>> = vec![] ;
            for _i in 0..self.grid_dim.0 * self.grid_dim.1{
                grid.push(vec![])
            }
            
            for (ind, ball) in self.balls.iter_mut().enumerate() {
                ball.update(dt);
                self.ke+=(ball.velocity).norm_squared();
            use std::cmp::{max, min};
            let x = max(min((ball.position.x / self.grid_size) as usize, self.grid_dim.0 - 1), 0);
            let y = max(min((ball.position.y / self.grid_size) as usize, self.grid_dim.1 - 1), 0);
            let index = x + y * self.grid_dim.0;
            grid[index].push(ind);
            
            }
            
            for i in 0..self.grid_dim.0*self.grid_dim.1{
                for x in -1..2{
                    for y in -1..2{
                        let r = (self.grid_dim.0 as i32 )*x+y+i as i32;
                        if r>=0 && r<(self.grid_dim.0*self.grid_dim.1) as i32{
                                for e1 in &grid[i]{
                                    for e2 in &grid[r as usize]{   {
                                        if e1==e2{continue;};
                                        let (b1, b2) = crate::ball::get_two_elements(&mut self.balls, *e1, *e2);
                                        b1.collide(b2);
                                    }
                            }
                        }
                    } 
                }
            }
        }

    }
    fn interact(&mut self){

    }
    pub fn draw(&mut self,canvas:&mut WindowCanvas){
        for ball in &self.balls {
            ball.draw(canvas);

        }
        // println!( "{}",self.ke );
        self.ke =0.0;
    }
}

}