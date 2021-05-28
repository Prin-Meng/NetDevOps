#!/bin/bash

set -e

influx <<-EOSQL
create retention policy "devdb_rp_policy" on "devdb" duration 3w replication 1 default
EOSQL