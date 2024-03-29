with temp as (
	select 
		divelogid,
		round(max(currentdepth),2) as max_depth_ft,
		round(avg(currentdepth),2) as avg_depth_ft,
		max(aiSensor0_PressurePSI) as max_PSI,
		min(aiSensor0_PressurePSI) as min_PSI,
		max(aiSensor0_PressurePSI)-min(aiSensor0_PressurePSI) as consumed_PSI,
	    (max(currenttime)-min(currenttime))/1000/60 as time_minutes

	from dive_log_records

	group by 1)
	
select 
	divelogid,
	avg_depth_ft,
	consumed_PSI,
	time_minutes,
	(consumed_PSI/time_minutes)*(33/(avg_depth_ft+33)) as SAC

from temp

group by 1
