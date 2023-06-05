BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "provinces_states" (
	"province_state_id"	INTEGER DEFAULT 1 UNIQUE,
	"province_state"	TEXT,
	"country_region_id"	INTEGER,
	FOREIGN KEY("country_region_id") REFERENCES "countries_regions"("country_region_id"),
	PRIMARY KEY("province_state_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "dates" (
	"dates_id"	INTEGER DEFAULT 1 UNIQUE,
	"observation_date"	TEXT NOT NULL,
	"last_update"	TEXT NOT NULL,
	PRIMARY KEY("dates_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "countries_regions" (
	"country_region_id"	INTEGER DEFAULT 1 UNIQUE,
	"country_region"	TEXT NOT NULL,
	PRIMARY KEY("country_region_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "records" (
	"record_id"	INTEGER DEFAULT 1 UNIQUE,
	"sno"	INTEGER NOT NULL,
	"country_region_id"	INTEGER,
	"dates_id"	INTEGER,
	FOREIGN KEY("dates_id") REFERENCES "dates"("dates_id"),
	FOREIGN KEY("country_region_id") REFERENCES "countries_regions"("country_region_id"),
	PRIMARY KEY("record_id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "statistics" (
	"statistics_id"	INTEGER DEFAULT 1 UNIQUE,
	"confirmed"	INTEGER NOT NULL,
	"deaths"	INTEGER NOT NULL,
	"recovered"	INTEGER NOT NULL,
	"record_id"	INTEGER,
	FOREIGN KEY("record_id") REFERENCES "records"("record_id"),
	PRIMARY KEY("statistics_id" AUTOINCREMENT)
);
COMMIT;
