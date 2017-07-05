from google.cloud import pubsub
while True:

    try:
        """Receives a message from a pull subscription."""
        pubsub_client = pubsub.Client()
        topic = pubsub_client.topic('earthquake-topic')
        subscription = topic.subscription('earthquake-subscription')

        # Change return_immediately=False to block until messages are
        # received.
        results = subscription.pull(return_immediately=True)
        messlen = len(results)
        if (messlen > 0):
            print('Received {} messages.'.format(messlen))

        for ack_id, message in results:
            print('* {}: {}, {}'.format(message.message_id, message.data, message.attributes))
            if results:
                subscription.acknowledge([ack_id for ack_id, message in results])
    except Exception as e: 
        print('Something went wrong')
        s = str(e)
        print(s)