from notification import NotificationMiddlewareHandler
import json

temp = {
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "_You_ have a new request:\n*<fakeLink.toEmployeeProfile.com|Fred Enriquez - New device request>*"
			}
		},
		{
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
					"text": "*Type:*\nComputer (laptop)"
				},
				{
					"type": "mrkdwn",
					"text": "*When:*\nSubmitted Aut 10"
				},
				{
					"type": "mrkdwn",
					"text": "*Last Update:*\nMar 10, 2015 (3 years, 5 months)"
				},
				{
					"type": "mrkdwn",
					"text": "*Reason:*\nAll vowel keys aren't working."
				},
				{
					"type": "mrkdwn",
					"text": "*Specs:*\n\"Cheetah Pro 15\" - Fast, really fast\""
				}
			]
		},
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Approve"
					},
					"style": "primary",
					"value": "click_me_123"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Deny"
					},
					"style": "danger",
					"value": "click_me_123"
				}
			]
		}
	]
}


def t_sns_1():
    sns = NotificationMiddlewareHandler.get_sns_client()
    print("Got SNS Client!")
    tps = NotificationMiddlewareHandler.get_sns_topics()
    print("SNS Topics = \n", json.dumps(tps, indent=2))

    message = {"cool": "beans"}
    NotificationMiddlewareHandler.send_sns_message(
        "arn:aws:sns:us-east-1:150198544176:SNS_user_changed",
        message
    )


def t_slack():

    NotificationMiddlewareHandler.send_slack_message(
        "Cool",  "Create",
                             {
                                 "uni": "dff9",
                                 "last_name": "Boring",
                                 "first_name": "Extremely"
                             }
    )

#t_sns_1()

t_slack()