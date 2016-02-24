#define MOT_A1 5
#define MOT_A2 6
#define MOT_B1 10
#define MOT_B2 11

#define BUT1 12
#define BUT2 13
#define BUT3 8

#define SPEED_STEPS 255

#define BAUD 9600

// describes a motor
struct motor {
	int pin1, pin2;
};

struct motor motor_a, motor_b;

// Initialize a motor struct.
void motor_init(struct motor *motor, int pin1, int pin2);

// Run a motor at speed, where -1.0 <= speed <= 1.0.
void motor_run(struct motor *motor, float speed);

// Brake a motor.
void motor_brake(struct motor *motor);

// Cause a motor to coast.
void motor_coast(struct motor *motor);

void setup()
{
	motor_init(&motor_a, MOT_A1, MOT_A2);
	motor_init(&motor_b, MOT_B1, MOT_B2);

	Serial.begin(BAUD);
}

void loop()
{
	// Example code: Run each motor back and forth at half speed.

	int time = 1000;
	float speed = 0.5;

	motor_run(&motor_a, speed);
	delay(time);
	motor_coast(&motor_a);
	delay(time);
	motor_run(&motor_a, -speed);
	delay(time);
	motor_coast(&motor_a);
	delay(time);

	motor_run(&motor_b, speed);
	delay(time);
	motor_coast(&motor_b);
	delay(time);
	motor_run(&motor_b, -speed);
	delay(time);
	motor_coast(&motor_b);
	delay(time);
}

void motor_init(struct motor *motor, int pin1, int pin2)
{
	motor->pin1 = pin1;
	motor->pin2 = pin2;

	pinMode(pin1, OUTPUT);
	pinMode(pin2, OUTPUT);

	motor_coast(motor);
}

void motor_run(struct motor *motor, float speed)
{
	int pin1_state, pin2_state;
	int speed_raw;

	if (speed < -1.0 || speed > 1.0)
		speed = 0.0;

	speed_raw = (int)(SPEED_STEPS * speed);

	if (speed_raw < 0)
		speed_raw *= -1;

	pin1_state = LOW;
	pin2_state = LOW;

	if (speed > 0.0)
		analogWrite(motor->pin1, speed_raw);
	else if (speed < 0.0)
		analogWrite(motor->pin2, speed_raw);

}

void motor_brake(struct motor *motor)
{
	digitalWrite(motor->pin1, HIGH);
	digitalWrite(motor->pin2, HIGH);
}

void motor_coast(struct motor *motor)
{
	digitalWrite(motor->pin1, LOW);
	digitalWrite(motor->pin2, LOW);
}
