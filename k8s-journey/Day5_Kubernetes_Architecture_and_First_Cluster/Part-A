==================================================================
DAY 5 - PART A: THEORY
Kubernetes Architecture and Your First Cluster
Time: 45-60 minutes
==================================================================

1. THE ANALOGY
--------------
Think of a restaurant.
- The CONTROL PLANE is management: it takes the orders, decides which
  cook handles each dish, and keeps track of everything.
- The WORKER NODES are the kitchen stations where the cooking happens.

You (the customer) never walk into the kitchen. You give your order to
the front desk (the API server), and the system makes it happen.


2. CONTROL PLANE COMPONENTS (THE BRAIN)
---------------------------------------
kube-apiserver
  The front door. Every kubectl command, and every internal component,
  talks to it over HTTPS (REST). It checks who you are, whether you are
  allowed, validates the request, and stores it.

etcd
  A distributed key-value database that holds the ENTIRE cluster state:
  every pod, service, secret, node. Only the API server talks to etcd.
  If etcd is lost without a backup, the cluster loses its memory.

kube-scheduler
  Watches for new pods that have no node assigned yet. It filters the
  nodes that can run the pod (enough CPU/memory, rules allow it) and
  scores them, then writes the chosen node name onto the pod.

kube-controller-manager
  Runs many "control loops" (controllers). Example: the ReplicaSet
  controller sees "3 replicas wanted, 2 exist" and creates 1 more.
  The node controller notices when a node stops responding.

cloud-controller-manager (only in cloud clusters)
  Talks to the cloud provider: creates load balancers, attaches disks,
  registers cloud VMs as nodes. You will meet it in Week 7.


3. WORKER NODE COMPONENTS (THE KITCHEN)
---------------------------------------
kubelet
  The agent running on every node (as a systemd service). It watches
  the API server for pods assigned to its node, tells the container
  runtime to start them, runs health checks, and reports status back.

Container runtime
  containerd or CRI-O. It pulls images and runs containers, using the
  same namespaces and cgroups you studied on Day 2. Kubernetes talks to
  it through the CRI (Container Runtime Interface).
  Note: Docker Engine is NOT used as the runtime in modern Kubernetes
  (removed in v1.24). Images built with Docker or Podman still work,
  because they follow the same OCI image standard.

kube-proxy
  Programs iptables (or IPVS) rules on each node so that traffic sent
  to a Service reaches one of its pods. Same NAT idea as Day 4.

CNI plugin (network plugin)
  Gives every pod an IP address and connects pods across nodes.
  kind uses "kindnet". Others: Calico, Cilium, Flannel (Week 3).


4. THE CORE IDEA: DESIRED STATE vs ACTUAL STATE
-----------------------------------------------
You do not tell Kubernetes "start container X on server Y".
You tell it WHAT YOU WANT:  "I want 3 copies of nginx running."

Controllers constantly compare:
    desired state (what you declared, stored in etcd)
    actual state  (what is really running)
and take action to close the gap. This never stops.

This is called the RECONCILIATION LOOP. Almost everything in Kubernetes
works this way. If a pod dies, the actual state (2) no longer matches
the desired state (3), so a controller creates a new pod.

    +-----------+      +------------+      +-------------+
    |  OBSERVE  | ---> |  COMPARE   | ---> |    ACT      |
    | (actual)  |      | (desired?) |      | (fix diff)  |
    +-----------+      +------------+      +-------------+
          ^                                       |
          +---------------------------------------+


5. KEY OBJECTS (JUST THE NAMES FOR NOW)
---------------------------------------
Pod         Smallest unit. Wraps one or more containers that share
            an IP address and storage.
Deployment  Keeps N copies of a pod running; does rolling updates.
Service     A stable IP and DNS name in front of a group of pods.
Namespace   A logical folder inside the cluster (dev, prod, ...).
Node        A machine (VM or physical) that runs pods.


6. TOOLS
--------
kubectl         The command-line client. It only ever talks to the
                API server.
kubeconfig      The file ~/.kube/config. Holds cluster addresses,
                credentials, and "contexts" (cluster + user pairs).
kind            "Kubernetes IN Docker". Runs each Kubernetes node as a
                container, so you can have a 3-node cluster on one
                laptop. Perfect for labs.


7. ARCHITECTURE PICTURE
-----------------------

            you --> kubectl
                       |
                       v  HTTPS
   +---------------- CONTROL PLANE ----------------+
   |  kube-apiserver  <---->  etcd                 |
   |       ^    ^                                  |
   |       |    +---- kube-scheduler               |
   |       +--------- kube-controller-manager      |
   +-------|---------------------------------------+
           | (everyone watches the API server)
     +-----+--------------------+
     v                          v
 +------- NODE 1 -------+  +------- NODE 2 -------+
 | kubelet              |  | kubelet              |
 | containerd           |  | containerd           |
 | kube-proxy           |  | kube-proxy           |
 | [pod] [pod]          |  | [pod] [pod] [pod]    |
 +----------------------+  +----------------------+


KEY POINTS TO REMEMBER
----------------------
- Only the API server talks to etcd.
- The scheduler decides WHERE a pod runs; the kubelet actually RUNS it.
- Kubernetes is declarative: you describe the goal, controllers do
  the work, forever.
