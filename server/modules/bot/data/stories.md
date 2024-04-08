## greeting
* greet
 - utter_greet
* greet
 - utter_greet
* mood_great
 - utter_great

## mood_great
* greet
 - utter_greet
* mood_unhappy
 - utter_unhappy

## mod_unhappy
* greet
 - utter_greet
* mood_unhappy
 - utter_unhappy
* affirm
 - utter_great

## headache
* greet
 - utter_greet
* health_headache
 - utter_headache
* pain_level
 - utter_schedule
* affirm
 - utter_affirm

## headache_again

* greet
 - utter_greet
* health_headache
 - utter_headache
* pain_level
 - utter_schedule
* deny
 - utter_deny
* affirm
 - utter_affirm

## stomachache_again
* greet
 - utter_greet
* health_stomachache
 - utter_stomachache
* pain_level
 - utter_schedule
* deny
 - utter_deny
* affirm
 - utter_affirm

## stomachache
* greet
 - utter_greet
* health_stomachache
 - utter_stomachache
* pain_level
 - utter_schedule
* affirm
 - utter_affirm

## floo
* greet
 - utter_greet
* health_floo
 - utter_floo
*affirm
 - utter_schedule
*affirm
 - utter_affirm

## floo_again
* greet
 - utter_greet
* health_floo
 - utter_floo
*affirm
 - utter_schedule
* deny
 - utter_deny
* affirm
 - utter_affirm
 
## need_help_unhappy
* greet
 - utter_greet
* need_help
 - utter_need_help
* mood_unhappy
 - utter_unhappy

## need_help_unhappy_to_happy
* greet
 - utter_greet
* need_help
 - utter_need_help
* mood_unhappy
 - utter_unhappy
* affirm
 - utter_affirm

## need_help_ambulance
* greet
 - utter_greet
* need_help
 - utter_need_help
* emergency_ambulance
 - utter_emergency_ambulance

## need_help_ambulance_answer
* greet
 - utter_greet
* need_help
 - utter_need_help
* emergency_ambulance
 - utter_emergency_ambulance
* affirm
 - utter_great

## need_help_stomachache_deny
* greet
 - utter_greet
* need_help
 - utter_need_help
* health_stomachache
 - utter_stomachache
* pain_level
 - utter_schedule
* deny
 - utter_deny
* affirm
 - utter_affirm

## need_help_stomachache
* greet
 - utter_greet
* need_help
 - utter_need_help
* health_stomachache
 - utter_stomachache
* pain_level
 - utter_schedule
* affirm
 - utter_affirm

## need_help_headache
* greet
 - utter_greet
* need_help
 - utter_need_help
* health_headache
 - utter_headache
* pain_level
 - utter_schedule
* affirm
 - utter_affirm

## need_help_headache_deny
* greet
 - utter_greet
* need_help
 - utter_need_help
* health_headache
 - utter_headache
* pain_level
 - utter_schedule
* affirm
 - utter_affirm
* deny
 - utter_deny
* affirm
 - utter_affirm

## need_help_floo
* greet
 - utter_greet
* need_help
 - utter_need_help
* health_floo
 - utter_floo
* affirm
 - utter_schedule
* affirm
 - utter_affirm

## need_help_floo_deny
* greet
 - utter_greet
* need_help
 - utter_need_help
* health_floo
 - utter_floo
* affirm
 - utter_schedule
* deny
 - utter_deny
* affirm
 - utter_affirm

## ambulance
* emergency_ambulance
 - utter_emergency_ambulance
* affirm
 - utter_affirm

## greet_ambulance
* greet
 - utter_greet
* emergency_ambulance
 - utter_emergency_ambulance
* affirm
 - utter_affirm
 
## emergency
* need_help
 - utter_need_help
* emergency_ambulance
 - utter_emergency_ambulance

## stomachache
* need_help
 - utter_need_help
* health_stomachache
 - utter_stomachache
* pain_level
 -utter_schedule
* affirm
 -utter_affirm

## headache
* need_help
 - utter_need_help
* health_headache
 - utter_headache
* pain_level
 - utter_schedule
* affirm
 - utter_affirm

## stomachache_reschedule
* need_help
 - utter_need_help
* health_stomachache
 - utter_stomachache
* pain_level
 - utter_schedule
* deny
 - utter_deny
* affirm
 - utter_affirm

## headache_reschedule
* need_help
 - utter_need_help
* health_headache
 - utter_headache
* pain_level
 -utter_schedule
* deny
 - utter_deny
* affirm
 - utter_affirm

## floo
* need_help
 - utter_need_help
* health_floo
 - utter_floo
* pain_level
 - utter_schedule
* affirm
 - utter_affirm


## floo_reschedule
* need_help
 - utter_need_help
* health_floo
 - utter_floo
* pain_level
 - utter_schedule
* deny
 - utter_deny
* affirm
 - utter_affirm


## stomachache_greet
* greet
 - utter_greet
* health_stomachache
 - utter_stomachache
* pain_level
 - utter_schedule
* affirm
 - utter_affirm

## headache_greet
* greet
 - utter_greet
* health_headache
 - utter_headache
* pain_level
 - utter_schedule
* affirm
 - utter_affirm

## stomachache_reschedule_greet
* greet
 - utter_greet
* health_stomachache
 - utter_stomachache
* pain_level
 - utter_schedule
* deny
 - utter_deny
* affirm
 - utter_affirm

## headache_reschedule_greet
* greet
 - utter_greet
* health_headache
 - utter_headache
* pain_level
 - utter_schedule
* deny
 - utter_deny
* affirm
 - utter_affirm

## floo_greet
* greet
 - utter_greet
* health_floo
 - utter_floo
* pain_level
 - utter_schedule
* affirm
 - utter_affirm


## floo_reschedule_greet
* greet
 - utter_greet
* health_floo
 - utter_floo
* pain_level
 - utter_schedule
* deny
 - utter_deny
* affirm
 - utter_affirm
