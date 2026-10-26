K8S JOURNEY - COURSE INDEX (Days 5-63)
========================================
Each day: Part-A = theory, Part-B = step-by-step lab, Part-C = checkpoint (fill in Ans:)
Days 1-4 are your existing folders.


WEEK 1: Containers and Your First Cluster
--------------------------------------------------
  Day5_Kubernetes_Architecture_and_First_Cluster
  Day6_The_Request_Flow_kubectl_run
  Day7_Revision_Tooling_and_Break_Fix

WEEK 2: Workloads
--------------------------------------------------
  Day8_YAML_Basics_and_Declarative_Model
  Day9_Pods_in_Depth_Init_and_Sidecar_Containers
  Day10_ReplicaSets_Labels_and_Selectors
  Day11_Deployments_and_Rolling_Updates
  Day12_Rollbacks_and_Revision_History
  Day13_Namespaces_and_Imperative_vs_Declarative_Workflow
  Day14_Week2_Checkpoint_Zero_Downtime_App

WEEK 3: Networking
--------------------------------------------------
  Day15_Kubernetes_Network_Model
  Day16_Services_ClusterIP_and_Endpoints
  Day17_DNS_in_Kubernetes_CoreDNS
  Day18_NodePort_LoadBalancer_and_kube-proxy
  Day19_Ingress_and_Ingress_Controllers
  Day20_CNI_Plugins_Calico_Cilium_Flannel
  Day21_Week3_Checkpoint_Frontend_Backend_Ingress

WEEK 4: Configuration and Storage
--------------------------------------------------
  Day22_ConfigMaps
  Day23_Secrets
  Day24_Volumes_emptyDir_and_hostPath
  Day25_PersistentVolumes_PVC_StorageClass
  Day26_StatefulSets
  Day27_Jobs_and_CronJobs
  Day28_Week4_Checkpoint_WordPress_MySQL

WEEK 5: Resources, Health, Scheduling, Security
--------------------------------------------------
  Day29_Requests_Limits_and_QoS
  Day30_OOMKill_and_CPU_Throttling
  Day31_Probes_Liveness_Readiness_Startup
  Day32_Scheduling_Affinity_Taints_DaemonSets
  Day33_RBAC_and_ServiceAccounts
  Day34_NetworkPolicies_and_Pod_Security
  Day35_Week5_Checkpoint_Secure_Team_Namespace

WEEK 6: Under the Hood and Troubleshooting
--------------------------------------------------
  Day36_Control_Plane_Internals_API_Server_and_etcd
  Day37_Scheduler_Controllers_and_Reconciliation
  Day38_kubeadm_Cluster_Part1_Prerequisites
  Day39_kubeadm_Cluster_Part2_Init_Join_CNI
  Day40_etcd_Backup_Restore_and_Cluster_Upgrade
  Day41_Troubleshooting_Methodology_Break_Fix
  Day42_Week6_Checkpoint_Fix_a_Broken_Cluster

WEEK 7: Kubernetes in the Cloud (AWS EKS)
--------------------------------------------------
  Day43_Cloud_Basics_Managed_vs_Self-Managed
  Day44_Create_a_Managed_Cluster_EKS
  Day45_Registries_and_Cloud_Load_Balancers
  Day46_Cloud_Storage_StorageClasses_and_Zones
  Day47_Cloud_IAM_for_Pods_Workload_Identity
  Day48_Autoscaling_HPA_and_Cluster_Autoscaler
  Day49_Cost_Cleanup_and_Production_Considerations

WEEK 8: Production Practices and Capstone
--------------------------------------------------
  Day50_Helm_Charts_Values_Releases
  Day51_Writing_Your_Own_Helm_Chart_and_Kustomize
  Day52_TLS_and_cert-manager
  Day53_Observability_Prometheus_Grafana_Alerts
  Day54_GitOps_with_Argo_CD
  Day55_CI_CD_Build_Push_Update_Manifests
  Day56_Capstone_3-Tier_App_End_to_End

WEEK 9: Extending Kubernetes (optional)
--------------------------------------------------
  Day57_Advanced_Job_Patterns_Parallelism_Retries_Cleanup
  Day58_Queue_Workers_Autoscaled_with_KEDA
  Day59_CNI_Deep_Dive_Calico_vs_Cilium
  Day60_CSI_Drivers_and_StorageClasses_Deep_Dive
  Day61_CRDs_Custom_Resources
  Day62_Operators_CloudNativePG
  Day63_Admission_Control_Kyverno_and_Course_Wrap-up

Clusters used:
  kind-lab     ~/k8s-journey/kind/kind-config.yaml (Days 5-18), kind-ingress.yaml (Day 19 on)
  kind-calico  ~/k8s-journey/kind/kind-calico.yaml (Days 20, 34-35, 59)
  kubeadm VMs  cp1/worker1/worker2 (Days 38-42)
  AWS EKS      ~/k8s-journey/cloud/eks/cluster.yaml (Days 43-49, optional on 56). DELETE IT DAILY.

