from datetime import datetime, timedelta

# Input webkit timestamp
webkit_timestamp = 13350778683284315

epoch_start = datetime(1601, 1, 1)
webkit_seconds = webkit_timestamp / 1e6
final_time = epoch_start + timedelta(seconds=webkit_seconds)

print(final_time)
