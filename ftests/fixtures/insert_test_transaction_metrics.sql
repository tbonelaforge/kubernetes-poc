INSERT INTO `transaction_metrics` (`sub_key`, `timestamp`, `period`, `publish_transactions`, `subscribe_transactions`, `subscribe_timeouts_transactions`, `subscribe_heartbeats_transactions`, `subscribe_clienterrors_transactions`, `publish_requests`, `subscribe_requests`, `subscribe_timeout_requests`, `subscribe_heartbeat_requests`, `subscribe_clienterrors_requests`)
VALUES
	('test_sub_key', 1483632000, 'hour', 42, 10727, 2835, 877, 551, 42, 10691, 2836, 877, 551),
	('test_sub_key', 1483635600, 'hour', 138, 103345, 10945, 2841, 2125, 138, 102236, 10952, 2842, 2125),
	('test_sub_key', 1483639200, 'hour', 182, 209660, 14978, 1884, 2280, 181, 208801, 14978, 1884, 2280),
	('test_sub_key', 1483642800, 'hour', 197, 212350, 13790, 2327, 1533, 197, 211346, 13790, 2327, 1533),
	('test_sub_key', 1483646400, 'hour', 48, 39959, 10899, 1739, 1173, 48, 39816, 10899, 1739, 1173),
	('test_sub_key', 1483650000, 'hour', 107, 87300, 10879, 811, 1188, 106, 86853, 10879, 811, 1188),
	('test_sub_key', 1483653600, 'hour', 61, 38345, 7045, 907, 1242, 60, 37931, 7045, 907, 1242),
	('test_sub_key', 1483657200, 'hour', 10, 4709, 5971, 638, 897, 10, 4709, 5971, 638, 897),
	('test_sub_key', 1483660800, 'day', 1, 331, 51381, 248, 3819, 1, 331, 51381, 248, 3562),
	('test_sub_key', 1483660800, 'hour', 0, 23, 4881, 7, 547, 0, 23, 4881, 7, 547),
	('test_sub_key', 1483664400, 'hour', 1, 308, 3650, 2, 288, 1, 308, 3654, 2, 288);
