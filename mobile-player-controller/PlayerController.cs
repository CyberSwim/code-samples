using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour {

	public float startSpeed, boostSpeed;

	[HideInInspector]
	public float startTime, finishTime;
	[HideInInspector]
	public bool levelFinished = false;
	[HideInInspector]
	public bool inStartZone;

	bool inSwingZone = false;
	bool inBoostZone = false;
	bool inBounceZone = false;
	[HideInInspector]
	public bool hasStarted = false;
	bool isTouching = false;

	Rigidbody2D rb;
	Rigidbody2D swing;
	FixedJoint2D swingFixed;
	HingeJoint2D jnt;

	PhysicsMaterial2D bounceMat;

	Touch touch0;


	void Start ()
	{
		rb = gameObject.GetComponent <Rigidbody2D> ();
		levelFinished = false;
	}

	void FixedUpdate ()
	{
		
		//Check for touch input
		if (Input.touchCount > 0) {
			touch0 = Input.GetTouch (0);
			isTouching = true;

			//Start boost
			if (inStartZone && hasStarted == false && touch0.phase == TouchPhase.Began) {
				rb.AddForce (Vector2.right * startSpeed, ForceMode2D.Impulse);
				hasStarted = true;
			}

			//Catch + release swings
			if (inSwingZone && (isTouching)) {
				//touch0.phase == TouchPhase.Stationary || touch0.phase == TouchPhase.Moved
				jnt = gameObject.AddComponent <HingeJoint2D> ();
				jnt.connectedBody = swing;
			} 

			if (touch0.phase == TouchPhase.Ended) {
				Destroy (jnt);
				isTouching = false;
			}

			if (inBounceZone) 
			{
				if (touch0.phase == TouchPhase.Began) 
				{
					bounceMat.bounciness = 1;
				}
			}
		}
		

		//Boosters
		if (inBoostZone) 
		{
			rb.AddForce (Vector2.right * boostSpeed);
		}
			
	}

	void OnTriggerEnter2D (Collider2D other)
	{
		if (other.CompareTag ("SwingZone"))
		{
			inSwingZone = true;
			swing = other.gameObject.GetComponent <Rigidbody2D> ();

			//Checks if swing is constrained, if true destroys constraint
			try
			{
				swingFixed = swing.GetComponentInChildren <FixedJoint2D> ();

				if (swingFixed != null)
				{
					Destroy (swingFixed);
				}
			}

			catch
			{
				return;
			}
		}

		//Check for boosters
		if (other.CompareTag ("BoostZone")) 
		{
			inBoostZone = true;
		}





		//Check for death
		if (other.CompareTag ("Killer"))
		{
				gameObject.SetActive (false);
		}

		//Check finish
		if (other.CompareTag ("Finish"))
		{
			hasStarted = false;
			finishTime = Time.time;
			levelFinished = true;
		}

		//Check for secret room
		if (other.CompareTag ("RoomTrigger")) 
		{
			GameObject sr = GameObject.FindGameObjectWithTag ("sRoom");
			sr.transform.position = new Vector2 (0, 0);
		}
	}

	void OnTriggerStay2D (Collider2D other)
	{
		//Check if player is at level start
		if (other.CompareTag ("Start"))
		{
			inStartZone = true;
		}


		if (other.CompareTag ("BounceZone")) 
		{
			EdgeCollider2D bounceColl = other.gameObject.GetComponentInChildren <EdgeCollider2D> ();
			bounceMat = bounceColl.GetComponent <PhysicsMaterial2D> ();

			inBounceZone = true;
		}
	}

	void OnTriggerExit2D (Collider2D other )
	{
		if (other.CompareTag ("SwingZone")) 
		{
			inSwingZone = false;
			swing = null;
		}

		if (other.CompareTag ("BoostZone")) 
		{
			inBoostZone = false;
		}

		if (other.CompareTag ("Start")) 
		{
			inStartZone = false;
			startTime = Time.time;
			levelFinished = false;
		}


		if (other.CompareTag ("BounceZone")) 
		{
			bounceMat.bounciness = 0;
			inBounceZone = false;

			if (bounceMat != null) 
			{
				bounceMat = null;
			}
		}


	}

}
